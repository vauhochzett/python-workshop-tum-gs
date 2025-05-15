import pytest

import tngpywo.lessons_01.lesson_gs_06_regex as target


@pytest.mark.parametrize(
    "haystack,needle,expected",
    [
        ("abc", "a", True),
        ("a", "a", True),
        ("this is it", "is", True),
        ("this is it", " is ", True),
        ("this isn't it", "welp", False),
    ],
)
def test_has_word(haystack, needle, expected):
    assert target.has_word(haystack, needle) == expected


@pytest.mark.parametrize("needle", ["a", "x"])
def test_has_word_return_type(needle):
    assert type(target.has_word("anything", needle)) is bool, (
        "Make sure to return a bool"
    )


@pytest.mark.parametrize(
    "haystack,needle,expected",
    [
        ("Where we're going, we don't need roads!", "do", 22),
        ("Something else", "do", -1),
        ("a", "a", 0),
        ("end", "d", 2),
    ],
)
def test_find_word(haystack, needle, expected):
    assert target.find_word(haystack, needle) == expected


@pytest.mark.parametrize(
    "given,expected",
    [
        (
            "Where we're going, we don't need roads!",
            ["e", "e", "e", "e", "o", "i", "e", "o", "e", "e", "o", "a"],
        ),
        ("aeiou", list("aeiou")),
        ("", []),
        ("xyz", []),
    ],
)
def test_fetch_vowels(given, expected):
    assert target.fetch_vowels(given) == expected


@pytest.mark.parametrize(
    "given",
    [
        "Where we're going, we don't need roads!",
        "No date here",
        "123-45-67",
        "2025-07-3",
        "25-03-2024",
    ],
)
def test_check_for_date_None(given):
    assert target.check_for_date(given) is None


@pytest.mark.parametrize(
    "given",
    ["Due date: 2025-07-03", "1900-01-01", "3500-02-28", "x2023-02-02yz"],
)
def test_check_for_date_Match(given):
    match = target.check_for_date(given)
    assert match is not None
    found = match.string[match.start() : match.end()]
    assert len(found) == 10


@pytest.mark.parametrize(
    "given,expected",
    [
        ("Where we're going, we don't need roads!", 0),
        ("I have a cat, a dog, and a dogdonkey!", 4),
        ("goosegoosegoosegoosegoosegoosegoosegoosegoosegoose", 10),
    ],
)
def test_count_animals(given, expected):
    assert target.count_animals(given) == expected


@pytest.mark.parametrize(
    "given",
    [
        "But this   does:!",
        "   xx:::",
        "   abcde::",
    ],
)
def test_check_for_pattern_True(given):
    assert target.check_for_pattern(given)


@pytest.mark.parametrize(
    "given",
    [
        "This doesn't contain it.",
        "This doesn't either",
        "  close:",
        "   but not: ",
        "   close.: enough",
    ],
)
def test_check_for_pattern_False(given):
    assert not target.check_for_pattern(given)


@pytest.mark.parametrize(
    "needle,expected",
    [
        ("need", True),
        ("going", True),
        ("do", False),
        ("road", False),
        ("roads", True),
    ],
)
def test_contains_as_word(needle, expected):
    haystack = "Where we're going, we don't need roads!"
    assert target.contains_as_word(haystack, needle) == expected


@pytest.mark.parametrize(
    "name_list,expected",
    [
        ("", ""),
        ("Lisa Frey, Lisa Maurer; Laura Mung... Lara F.", "Lisa"),
        ("LaraLaraLaraLauraLisa", "Lara"),
        ("Lisa", "Lisa"),
    ],
)
def test_find_most_common_name(name_list, expected):
    assert target.find_most_common_name(name_list) == expected
