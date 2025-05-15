import pytest

from tngpywo.lessons_01 import lesson_gs_02_containers_slicing as target
from tngpywo.tests.tools_for_testing import (
    assert_contains_code_pattern,
)


@pytest.mark.parametrize("in_and_out", [[1, 2, 3], [9, 8, 7], [5, 5, 5]])
def test_a_list(in_and_out):
    assert target.a_list(*in_and_out) == in_and_out


def test_your_first_element():
    assert "first" == target.your_first_element(["first", "second", "last"])
    assert "only element" == target.your_first_element(["only element"])
    with pytest.raises(IndexError):
        target.your_first_element([])
        pytest.fail("What did you do? Just return data[0] and be done.")


@pytest.mark.parametrize("data,expected", [([1, 2, 3], 3), (["a", "b", "c"], "c")])
def test_get_last_element(data, expected):
    assert target.get_last_element(data) == expected


def test_return_some_dict():
    assert {"KEY": "VAL", "key2": "val2"} == target.return_some_dict(
        "KEY", "VAL", "key2", "val2"
    )
    assert {1: 2, 3: 4} == target.return_some_dict(1, 2, 3, 4)


def test_return_dict_keys():
    assert ["a", "b", "c"] == sorted(target.return_dict_keys({"a": 1, "b": 2, "c": 3}))
    assert [] == list(target.return_dict_keys({}))


def test_first_and_last():
    assert target.first_and_last([1, 2, 3]) == [1, 3]
    assert target.first_and_last(["a"]) == ["a", "a"]
    assert_contains_code_pattern(
        target.first_and_last, "?[-1]", "Use [-1] to get the last element"
    )


def test_remove_from_dict():
    d = {"a": 1, "b": 2, "c": 3}
    target.remove_from_dict(d)
    assert {"b": 2, "c": 3} == d

    d = {"a": 1}
    target.remove_from_dict(d)
    assert {} == d


@pytest.mark.parametrize(
    "data,start,end,expected",
    [([1, 2, 3], 1, 2, [2, 3]), (["a", "b"], 0, 1, ["a", "b"])],
)
def test_slicing_it(data, start, end, expected):
    assert target.slicing_it(data, start, end) == expected


def test_return_dict_values():
    assert [6, 7, 8] == sorted(target.return_dict_values({"T": 6, "G": 7, "B": 8}))
    assert [] == list(target.return_dict_values({}))


def test_without_first_and_last():
    assert "bcdefgh" == target.without_first_and_last("abcdefghi")
    assert list(range(1, 999)) == target.without_first_and_last(list(range(1000)))

    assert_contains_code_pattern(
        target.without_first_and_last,
        "?[1:-1]",
        "In Python sequence indices can be slice objects (begin:end:step), not just integers",
    )
