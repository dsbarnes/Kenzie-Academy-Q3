import unittest
import subprocess


class TestPep8(unittest.TestCase):
    def test_flake8(self):
        ret_code = subprocess.call(["flake8", "snake.py"])
        self.assertEqual(
            ret_code, 0, "There are still PEP 8 style guide violations")


if __name__ == "__main__":
    unittest.main()
