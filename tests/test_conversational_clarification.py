"""Offline safeguards for external-reference adaptation; no clinical data or private cases."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = [
    "docs/research/HOPEBOT_RESEARCH_NOTE_2026.md",
    "framework/consentful_conversational_structuring.md",
    "prompts/clarify-before-claim.md",
]


class HopeBotAdaptationTests(unittest.TestCase):
    def test_references_exist(self):
        for path in FILES:
            text = (ROOT / path).read_text(encoding="utf-8")
            self.assertGreater(len(text), 500, path)
            for dest in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                link = dest.split("#", 1)[0]
                if not link or "://" in link or link.startswith(("#", "mailto:")):
                    continue
                resolved = (ROOT / path).parent.joinpath(link).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT.resolve()), (path, link))
                self.assertTrue(resolved.is_file(), (path, link))

    def test_clarification_is_optional_not_clinical(self):
        method = (ROOT / FILES[1]).read_text(encoding="utf-8")
        prompt = (ROOT / FILES[2]).read_text(encoding="utf-8")
        for term in ("本人明确希望", "UNKNOWN", "不适用", "临床", "隐私"):
            self.assertIn(term, method)
        for term in ("不想回答", "NO_MODEL_CHANGE", "RETRACTION"):
            self.assertIn(term, prompt)

    def test_scientific_boundaries_are_preserved(self):
        notes = (ROOT / FILES[0]).read_text(encoding="utf-8")
        for term in ("132", "20", "一致性", "零分", "外部研究"):
            self.assertIn(term, notes)
        self.assertIn("PHQ-9", notes)
        self.assertIn("不照搬语料与代码", notes)


if __name__ == "__main__":
    unittest.main()
