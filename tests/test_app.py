import os
import sys
from pathlib import Path
import unittest
from unittest.mock import patch


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from app import payload  # noqa: E402


class App03Tests(unittest.TestCase):
    def test_health(self):
        self.assertEqual(payload("/healthz"), (200, {"status": "healthy"}))

    def test_secret_is_only_reported_as_loaded(self):
        with patch.dict(os.environ, {"API_KEY": "do-not-return-me"}):
            status, body = payload("/")
        self.assertEqual(status, 200)
        self.assertTrue(body["secret_loaded"])
        self.assertNotIn("do-not-return-me", str(body))


if __name__ == "__main__":
    unittest.main()
