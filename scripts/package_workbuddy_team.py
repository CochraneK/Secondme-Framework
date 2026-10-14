#!/usr/bin/env python3
"""Build a WorkBuddy Expert Team ZIP from ONLY this public repository's agents.

No private person data, no API keys, no network, no dependencies beyond stdlib.
This is a locally buildable integration; upload/publishing requires user action.
"""
from __future__ import annotations

import argparse
import json
import math
import struct
import zlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_AGENTS = ROOT / ".codebuddy" / "agents"
SOURCE_SKILLS = ROOT / ".codebuddy" / "skills"
AGENTS = (
    "secondme-team-lead",
    "secondme-guide",
    "secondme-evidence",
    "secondme-critic",
    "secondme-longitudinal",
    "secondme-editor",
    "secondme-privacy",
)
SKILLS = ("secondme-discovery", "secondme-output")
PLUGIN = "secondme-expert-team"
ROLES = (
    ("SecondMe Lead", "SecondMe 主理人", "Personal Understanding Orchestrator", "个人理解主理人", "lead"),
    ("Discovery Guide", "探索引导", "Adaptive Exploration Guide", "探索引导专家", "member"),
    ("Evidence Reviewer", "证据审查", "Provenance Reviewer", "事实来源专家", "member"),
    ("Model Challenger", "反证专家", "Competing Model Reviewer", "模型竞争专家", "member"),
    ("Time Historian", "纵向演化", "Longitudinal Model Historian", "时间修订专家", "member"),
    ("Report Editor", "报告主编", "Output Report Architect", "完整报告编辑", "member"),
    ("Privacy Guardian", "隐私审查", "Privacy and Agency Guardian", "隐私与主体性专家", "member"),
)


def _png_chunk(kind: bytes, data: bytes) -> bytes:
    return (struct.pack(">I", len(data)) + kind + data
            + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff))


def avatar_png(role: int, size: int = 512) -> bytes:
    """Generate a non-photographic geometric PNG icon, no portraits or fonts."""
    scan = bytearray()
    for y in range(size):
        scan.append(0)  # PNG row filter = None
        for x in range(size):
            dx, dy = x - size / 2, y - size / 2
            r = math.hypot(dx, dy)
            angle = math.atan2(dy, dx)
            swirl = math.cos((role + 3) * angle)
            on_ring = (90 + role * 4 < r < 155 + role * 2)
            on_detail = (r < 66 and swirl > 0.2)
            if on_ring or on_detail:
                value = 55 + ((role * 17) % 45)
                scan.extend((value, value, value + 5, 255))
            elif r < 177:
                scan.extend((232, 232, 236, 255))
            else:
                scan.extend((249, 249, 251, 255))
    header = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + _png_chunk(b"IHDR", header) + _png_chunk(
        b"IDAT", zlib.compress(bytes(scan), level=8)
    ) + _png_chunk(b"IEND", b"")


def manifest() -> dict:
    first = {
        "zh": "我不知道该怎么认识自己，请引导我从一件普通的小事开始。",
        "en": "I don't know how to explore myself. Please start with one ordinary event.",
    }
    members = []
    for role, details in zip(AGENTS, ROLES):
        en, zh, prof_en, prof_zh, kind = details
        members.append({
            "id": role,
            "name": {"en": en, "zh": zh},
            "profession": {"en": prof_en, "zh": prof_zh},
            "avatar": f"avatars/{role}.png",
            "role": kind,
        })
    result = {
        "name": PLUGIN,
        "version": "0.1.0",
        "description": "Evidence-aware, person-specific self-exploration and full-output expert team.",
        "author": {
            "name": "SecondMe Framework contributors",
            "email": "maintainer@example.com",
        },
        "agents": [f"./agents/{name}.md" for name in AGENTS],
        "skills": [f"./skills/{name}" for name in SKILLS],
        "expertType": "team",
        "agentName": AGENTS[0],
        "teamInfo": {"leadAgent": AGENTS[0], "memberAgents": list(AGENTS[1:])},
        "displayName": {"en": "SecondMe Expert Team", "zh": "SecondMe 个人探索专家团"},
        "profession": {"en": "Personal Reflection and Evidence Team", "zh": "个人探索与证据分析团队"},
        "displayDescription": {
            "en": "Guided, evidence-aware self-exploration with optional independent reviewers and personalized full-output reports.",
            "zh": "从普通对话发现好问题，按需审查证据、反例和长期变化，生成个性化完整报告，尊重隐私与主体性。",
        },
        "avatar": "avatars/team.png",
        "categoryId": "15-Education",
        "defaultInitPrompt": first,
        "plugin": PLUGIN,
        "homepage": "https://github.com/CochraneK/Secondme-Framework",
        "license": "MIT",
        "tags": [
            {"en": "Self-reflection", "zh": "自我探索"},
            {"en": "Evidence reasoning", "zh": "证据推理"},
            {"en": "Longitudinal reports", "zh": "长期报告"},
        ],
        "quickPrompts": [
            first,
            {"en": "Give me three useful questions I might overlook.", "zh": "推荐三个我可能想不到、但有价值的问题。"},
            {"en": "Create an evidence-based long-form report from my available notes.", "zh": "根据我提供的记录，做一份证据充分的完整人物报告。"},
        ],
        "members": members,
    }
    return result


def bundle(destination: Path) -> Path:
    """Only explicit public source paths are copied into the package."""
    items: dict[str, bytes] = {}
    for name in AGENTS:
        source = SOURCE_AGENTS / (name + ".md")
        if not source.is_file() or source.is_symlink():
            raise ValueError(f"Missing/unsafe public agent source: {source}")
        data = source.read_bytes()
        if not data.startswith(b"---\n"):
            raise ValueError(f"Agent missing frontmatter: {name}")
        items[f"agents/{name}.md"] = data
    for name in SKILLS:
        source = SOURCE_SKILLS / name / "SKILL.md"
        if not source.is_file() or source.is_symlink():
            raise ValueError(f"Missing/unsafe public skill source: {source}")
        items[f"skills/{name}/SKILL.md"] = source.read_bytes()

    config = manifest()
    assert config["agentName"] == config["teamInfo"]["leadAgent"]
    assert len(config["tags"]) == len(config["quickPrompts"]) == 3
    assert config["defaultInitPrompt"] == config["quickPrompts"][0]
    items[".codebuddy-plugin/plugin.json"] = (json.dumps(
        config, ensure_ascii=False, indent=2
    ) + "\n").encode("utf-8")
    items["settings.json"] = (json.dumps(
        {"agent": AGENTS[0]}, ensure_ascii=False, indent=2
    ) + "\n").encode("utf-8")
    items["README.md"] = (
        "# SecondMe Expert Team\n\n"
        "Fully synthetic/public instructions; does not contain user records.\n"
        "Bring your own private notes only after reviewing your chosen runtime's privacy terms.\n"
        "The maintainer@example.com email is a publishing placeholder and must be replaced\n"
        "before applying for marketplace distribution.\n"
        "This is not a clinical diagnosis or autonomous cross-session memory system.\n"
    ).encode("utf-8")
    items["avatars/team.png"] = avatar_png(0)
    for i, agent in enumerate(AGENTS, 1):
        items[f"avatars/{agent}.png"] = avatar_png(i)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path, data in sorted(items.items()):
            zf.writestr(path, data)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="dist/secondme-expert-team.zip")
    args = parser.parse_args()
    path = bundle(Path(args.output))
    print("Built WorkBuddy team package:", path)
    print("Contains public agents/skills, synthetic avatars, plugin.json and settings.json.")
    print("IMPORTANT: replace placeholder author email before marketplace publishing.")


if __name__ == "__main__":
    main()
