import unittest
from unittest import TestCase
from unittest.mock import patch

import tngpywo.lessons_01.lesson_gs_07_exceptions as target


class TestExceptionHandling(TestCase):

    def test_demo_index_error(self):
        assert target.demo_index_error() == ["This", "is", "a", "sentence"]


    def test_get_element_from_list(self):
        my_list = ["This", "is", "a", "sentence"]

        assert target.get_element_from_list(my_list, 0) == "This"
        assert target.get_element_from_list(my_list, 5) == "Invalid!"


    def test_validate_age(self):
        self.assertTrue(target.validate_age(25))
        with self.assertRaises(ValueError):
            target.validate_age(-5)


    def test_safe_divide(self):
        self.assertEqual(target.safe_divide(10, 2), 5.0)
        self.assertEqual(target.safe_divide(5, 0), 0)
        self.assertEqual(target.safe_divide(0, 5), 0.0)


    @patch('builtins.open', side_effect=FileNotFoundError())
    def test_read_file_contents_not_found(self, mock_open):
        result = target.read_file_contents("missing.txt")
        self.assertEqual(result, '')


    def test_demo_name_error(self):
        assert target.demo_name_error() == 34


    def test_demo_type_error(self):
        assert target.demo_type_error(50, "Cent") == "50Cent"


    def test_demo_key_error(self):
        assert target.demo_key_error() == 16


    def test_demo_value_error(self):
        result = target.demo_value_error()
        assert len(result) == 5, "The resulting dict should contain five elements."
        assert result.pop("a") == "1"
        assert result.pop("b") == "22"
        assert result.pop("c") == "-2"
        assert result.pop("q") == "4"
        assert list(result.values())[0] == "5"


if __name__ == "__main__":
    unittest.main()