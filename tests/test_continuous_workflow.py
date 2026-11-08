"""Public v0.5 documentation contract: paths, lifecycle and safeguards.

Fully synthetic checks. No personal SecondMe data is needed or fetched.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW_MARKDOWN = [
    "framework/continuous_model_pipeline.md",
    "framework/entity_attribution_and_corrections.md",
    "framework/question_atlas_method.md",
    "framework/report_to_visual.md",
    "prompts/initialize-private-secondme.md",
    "prompts/capture-model-delta.md",
    "prompts/build-question-atlas.md",
    "prompts/create-visual-deck.md",
    "templates/EVIDENCE_CARD_TEMPLATE.md",
    "templates/CLAIM_LEDGER_TEMPLATE.md",
    "templates/ENTITY_REGISTER_TEMPLATE.md",
    "templates/QUESTION_ATLAS_TEMPLATE.md",
    "templates/VISUAL_REPORT_TEMPLATE.md",
    "templates/OUTPUT_CHANGELOG_TEMPLATE.md",
    "docs/CONTINUOUS_USE.md",
    "examples/fictional_longitudinal_cycle.md",
]
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class ContinuousWorkflowTests(unittest.TestCase):
    def test_public_v05_installable_markdown(self):
        record = json.loads(
            (ROOT / ".secondme/framework-manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(record["version"], "0.5.0")
        for p in NEW_MARKDOWN:
            full = ROOT / p
            self.assertTrue(full.exists(), p)
            self.assertGreater(full.stat().st_size, 100, p)
            if p.startswith(("framework/", "prompts/", "templates/")):
                self.assertIn(p, record["files"], p)
            else:
                self.assertNotIn(p, record["files"], p)

    def test_relative_links_resolve(self):
        for p in NEW_MARKDOWN:
            content = (ROOT / p).read_text(encoding="utf-8")
            for link in LINK_PATTERN.findall(content):
                target = link.split("#", 1)[0]
                if not target or "://" in target or target.startswith(
                    ("#", "mailto:", "tel:")
                ):
                    continue
                resolved = (ROOT / p).parent.joinpath(target).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT.resolve()), (p, link))
                self.assertTrue(resolved.is_file(), (p, link))

    def test_attribution_and_consent_are_not_optional(self):
        correction = (ROOT / "framework/entity_attribution_and_corrections.md").read_text(
            encoding="utf-8"
        )
        pipeline = (ROOT / "framework/continuous_model_pipeline.md").read_text(
            encoding="utf-8"
        )
        deck = (ROOT / "framework/report_to_visual.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("RETRACTED", correction)
        self.assertIn("speaker", correction)
        self.assertIn("NO_MODEL_CHANGE", pipeline)
        self.assertIn("获授权", pipeline)
        self.assertIn("可编辑", deck)
        self.assertIn("分享", deck)


if __name__ == "__main__":
    unittest.main()
