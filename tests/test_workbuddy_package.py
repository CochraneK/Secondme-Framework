"""WorkBuddy expert-team package integrity and privacy-safe structure."""
from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.package_workbuddy_team import AGENTS, SKILLS, avatar_png, bundle, manifest


class WorkBuddyPackageTests(unittest.TestCase):
    def test_manifest_team_contract(self):
        data = manifest()
        self.assertEqual(data["expertType"], "team")
        self.assertEqual(data["agentName"], data["teamInfo"]["leadAgent"])
        self.assertEqual(data["teamInfo"]["memberAgents"], list(AGENTS[1:]))
        self.assertEqual(len(data["members"]), len(AGENTS))
        self.assertEqual(len(data["quickPrompts"]), 3)
        self.assertEqual(len(data["tags"]), 3)
        self.assertEqual(data["defaultInitPrompt"], data["quickPrompts"][0])
        self.assertEqual(data["plugin"], data["name"])
        self.assertEqual(data["categoryId"], "15-Education")

    def test_pure_standard_library_bundle(self):
        with tempfile.TemporaryDirectory() as temp:
            path = bundle(Path(temp) / "public-team.zip")
            self.assertTrue(path.exists())
            with zipfile.ZipFile(path) as archive:
                names = set(archive.namelist())
                self.assertIn(".codebuddy-plugin/plugin.json", names)
                self.assertIn("settings.json", names)
                self.assertIn("avatars/team.png", names)
                self.assertEqual(
                    {n for n in names if n.startswith("agents/")},
                    {f"agents/{a}.md" for a in AGENTS},
                )
                for agent in AGENTS:
                    src = archive.read(f"agents/{agent}.md").decode()
                    self.assertIn(f"name: {agent}", src)
                    self.assertTrue(src.startswith("---\n"))
                    avatar = archive.read(f"avatars/{agent}.png")
                    self.assertTrue(avatar.startswith(b"\x89PNG\r\n\x1a\n"))
                    self.assertLess(len(avatar), 500000)
                for skill in SKILLS:
                    self.assertIn(f"skills/{skill}/SKILL.md", names)
                for name in names:
                    self.assertFalse(name.startswith("my/"), name)
                    self.assertFalse(name.startswith("custom/"), name)
                    self.assertFalse(name.startswith("examples/"), name)
                    self.assertFalse("PRIVATE" in name, name)
                self.assertEqual(
                    json.loads(archive.read(".codebuddy-plugin/plugin.json")),
                    manifest(),
                )
                self.assertEqual(
                    json.loads(archive.read("settings.json"))["agent"], AGENTS[0]
                )


if __name__ == "__main__":
    unittest.main()
