import pytest

from tngpywo.lessons_01 import lesson_gs_01_getting_started as target


def test_version_defined():
    result = target.version()
    assert "tng_0.0.2" == result


def test_working_with_variables():
    assert target.working_with_variables() == 500


def test_your_first_calculation():
    values = [-10, -5, 0, 5, 10]
    expected_results = [-2005, -255, -5, 245, 1995]
    for val, expected in zip(values, expected_results):
        result = target.your_first_calculation(val)
        assert result == expected


@pytest.mark.parametrize(
    "x,expected", [(10, True), (29, False), (11, False), (10.9, True)]
)
def test_floating_around(x, expected):
    assert target.floating_around(x) == expected


def test_convert_to_string():
    assert "I have 5 sheep" == target.insert_into_string(5)
    assert "I have cinque sheep" == target.insert_into_string("cinque")
    assert "I have  sheep" == target.insert_into_string("")


def test_join_arguments():
    assert "a-b" == target.join_arguments("a", "b", "-")
    assert "a?b" == target.join_arguments("a", "b", "?"), (
        "the custom separator is not used"
    )
    assert "1-b" == target.join_arguments(1, "b", "-"), (
        "it would be nice if your function would also work with integers"
    )
    assert "[1, 2, 3]-1.5" == target.join_arguments([1, 2, 3], 1.5, "-"), (
        "it would be nice if your function would also work with other types"
    )


@pytest.mark.parametrize(
    "x,expected", [(5, False), (5.0, True), (1, False), ("", False), (99.9, True)]
)
def test_is_float(x, expected):
    assert target.is_float(x) == expected


@pytest.mark.parametrize(
    "x,expected", [(5, True), (5.0, True), (1, True), ("", False), ([], False)]
)
def test_is_number(x, expected):
    assert target.is_number(x) == expected


@pytest.mark.parametrize(
    "left,right,expected",
    [
        (True, True, False),
        (True, False, True),
        (False, True, True),
        (False, False, False),
    ],
)
def test_xor(left, right, expected):
    assert target.xor(left, right) == expected
