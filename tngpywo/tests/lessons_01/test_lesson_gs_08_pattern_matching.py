import pytest

import tngpywo.lessons_01.lesson_gs_08_pattern_matching as target


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Adam", "Adam"),
        ("Mara Max", "Mara"),
        ("Sebas Gonzales Martines", "Sebas"),
    ],
)
def test_get_first_name(name, expected):
    assert target.get_first_name(name) == expected


@pytest.mark.parametrize(
    "command,expected",
    [
        ("shout", "AAAAH!"),
        ("count to 3", [0, 1, 2, 3]),
        ("count to 1", [0, 1]),
        ("is dog in doghouse", True),
        ("is cat in doghouse", False),
    ],
)
def test_handle_command(command, expected):
    assert target.handle_command(command) == expected


@pytest.mark.parametrize("cmd", ["typo", "other", ""])
def test_handle_command_ValueError(cmd):
    with pytest.raises(ValueError):
        target.handle_command(cmd)
