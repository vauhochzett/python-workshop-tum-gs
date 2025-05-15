import os
import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

import tngpywo.lessons_01.lesson_gs_05_process_files as target

MODULE_NAME = "tngpywo.lessons_01.lesson_gs_05_process_files"


class TestStringMethods(TestCase):
    def setUp(self):
        # Common test file setup
        self.test_file = "test_file.txt"
        self.cleanup_files = []

    def tearDown(self):
        # Clean up test files
        for f in self.cleanup_files:
            if os.path.exists(f):
                os.remove(f)

    def test_write_three_lines(self):
        # Test file creation and content
        target.write_three_lines(self.test_file)
        self.cleanup_files.append(self.test_file)

        self.assertTrue(os.path.exists(self.test_file))

        with open(self.test_file) as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 3)
            self.assertEqual(lines[0].strip(), "First line")
            self.assertEqual(lines[1].strip(), "Second line")
            self.assertEqual(lines[2].strip(), "Third line")

    def test_count_file_lines(self):
        # Test empty file
        with open(self.test_file, "w") as f:
            pass
        self.cleanup_files.append(self.test_file)
        self.assertEqual(target.count_file_lines(self.test_file), 0)

        # Test single line file
        with open(self.test_file, "w") as f:
            f.write("single line\n")
        self.assertEqual(target.count_file_lines(self.test_file), 1)

        # Test multi-line file
        with open(self.test_file, "w") as f:
            f.writelines(["line1\n", "line2\n", "line3\n"])
        self.assertEqual(target.count_file_lines(self.test_file), 3)

    def test_print_odd_lines(self):
        # Create test file
        with open(self.test_file, "w") as f:
            f.writelines([
                "line1\n",
                "line2\n",
                "line3\n",
                "line4\n",
                "line5\n"
            ])
        self.cleanup_files.append(self.test_file)

        # Capture printed output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            target.print_odd_lines(self.test_file)
            output = fake_out.getvalue().strip().split('\n')

            self.assertEqual(len(output), 3)
            self.assertEqual(output[0], "line1")
            self.assertEqual(output[1], "line3")
            self.assertEqual(output[2], "line5")


if __name__ == "__main__":
    unittest.main()
