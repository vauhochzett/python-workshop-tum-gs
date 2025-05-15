import unittest
from unittest import TestCase

import pytest

import tngpywo.lessons_01.lesson_gs_04_functions as target
from tngpywo.tests.tools_for_testing import check_calls_function


def test_add():
    assert target.add(1, 2) == 3
    assert target.add(-1, 1) == 0


def test_outer():
    assert target.outer(1, 2) == 3
    assert target.outer(-1, 1) == 0


def test_outer_calls_add():
    assert check_calls_function(target.outer, "add"), (
        "Your code does not call the function 'add()'"
    )


def _get_function(name):
    subtract = getattr(target, name, None)
    if subtract is None:
        pytest.fail(f'You did not define a function "{name}()"')
    return subtract


def test_subtract():
    subtract = _get_function("subtract")

    try:
        assert subtract(5, 3) == 2
    except TypeError:
        pytest.fail('Your function "subtract()" should have two parameters')


@pytest.mark.parametrize(
    "cmd,left,right,expected",
    [("add", 12, -12, 0), ("subtract", -12, -12, 0), ("multiply", 1, 0, "ERROR!")],
)
def test_handle(cmd, left, right, expected):
    handle = _get_function("handle")

    try:
        assert handle(cmd, left, right) == expected
    except TypeError:
        pytest.fail('Your function "handle()" should have three parameters')


class TestLessonFunctions(TestCase):
    def test_create_adder(self):
        add_three = target.create_adder(3)
        self.assertEqual(add_three(5), 8)

    def test_apply_twice(self):
        def add_one(x):
            return x + 1

        self.assertEqual(target.apply_twice(add_one, 5), 7)

    def test_create_greeter(self):
        hello = target.create_greeter("Hello")
        self.assertEqual(hello("Alice"), "Hello, Alice!")
        hi = target.create_greeter("Hi")
        self.assertEqual(hi("Bob"), "Hi, Bob!")

    def test_create_incrementor(self):
        d = {"data": 0}
        incrementor_1 = target.create_incrementor(d, "data")
        incrementor_1(5)
        self.assertEqual({"data": 5}, d)
        incrementor_1(10)
        self.assertEqual({"data": 15}, d)

        d = {"value": "start"}
        incrementor_2 = target.create_incrementor(d, "value")
        incrementor_2("XXX")
        self.assertEqual({"value": "startXXX"}, d)
        incrementor_2("YYY")
        self.assertEqual({"value": "startXXXYYY"}, d)

        d = {"data": 0}
        incrementor_3 = target.create_incrementor(d, "data")
        resulting_dict = incrementor_3(2)
        self.assertIs(d, resulting_dict)


if __name__ == "__main__":
    unittest.main()
