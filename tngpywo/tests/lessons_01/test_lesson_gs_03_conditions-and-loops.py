import io
import pytest
from contextlib import redirect_stdout

from tngpywo.lessons_01 import lesson_gs_03_conditions_and_loops as target


@pytest.mark.parametrize(
    "input,expected,message",
    [
        (42, "HIT", ""),
        (0, "OK", "for other non-negative numbers the function should return 'OK'"),
        (1, "OK", "for other non-negative numbers the function should return 'OK'"),
        (-1, "FAIL", "for negative numbers the function should return 'FAIL'")
    ],
)
def test_your_first_if_clause(input, expected, message):
    std_out = io.StringIO()

    with redirect_stdout(std_out):
        target.your_first_if_clause(input)
        assert std_out.getvalue() == f"{expected}\n", message


@pytest.mark.parametrize(
    "input,expected",
    [
        ((5, 0, 10), True),
        ((3, 0, 5), True),
        ((5, 5, 5), True),
        ((5, 3, 4), False),
        ((5, 6, 7), False),
        (("d", "a", "z"), True),
        (("d", "d", "d"), True),
        (("d", "e", "f"), False),
        (("d", "b", "c"), False)
    ],
)
def test_your_second_if(input, expected):
    std_out = io.StringIO()

    with redirect_stdout(std_out):
        target.your_second_if(*input)
        assert std_out.getvalue() == f"{expected}\n"


def test_your_first_for_loop():
    std_out = io.StringIO()
    with redirect_stdout(std_out):
        target.your_first_for_loop("Hello", 5)

    assert "Hello\nHello\nHello\nHello\nHello\n" == std_out.getvalue()


def test_count_to_n():
    std_out = io.StringIO()

    with redirect_stdout(std_out):
        target.count_to_n(3)
    assert "1\n2\n3\n" == std_out.getvalue()


def test_count_to_n_works_with_zero():
    std_out = io.StringIO()

    with redirect_stdout(std_out):
        target.count_to_n(0)
    assert "" == std_out.getvalue()


def test_your_second_for_loop():
    std_out = io.StringIO()
    with redirect_stdout(std_out):
        target.your_second_for_loop("Python is great!")

    assert "P\ny\nt\nh\no\nn\n" == std_out.getvalue()


@pytest.mark.parametrize(
    "input,expected",
    [
        (10, 15),
        (0, 1),
        (3, 6)
    ],
)
def test_sum_until_limit(input, expected):
    std_out = io.StringIO()

    with redirect_stdout(std_out):
        target.sum_until_limit(input)
        assert std_out.getvalue() == f"{expected}\n"
