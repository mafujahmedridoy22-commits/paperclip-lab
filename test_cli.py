import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class CliTests(unittest.TestCase):
    def test_hello_prints_greeting(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "cli.py"), "hello", "Alice"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, Alice!")

    def test_hello_missing_name_exits_with_code_2(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "cli.py"), "hello"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
