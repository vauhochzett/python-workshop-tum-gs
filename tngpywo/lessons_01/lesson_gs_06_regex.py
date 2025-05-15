"""
This lesson makes use of the re module in the Python standard library.
No need to remember everything, feel free to check the documentation:
https://docs.python.org/3/library/re.html
"""

import re

from tngpywo import raise_exercise_not_yet_started


def has_word(haystack, needle):
    """
    #core - intermediate

    Check if the word `needle` is in the `haystack`. Return a bool.

    >>> has_word("Where we're going, we don't need roads!", "do")
    True

    >>> has_word("Where we're going, we don't need roads!", "don't")
    True

    >>> has_word("Where we're going, we don't need roads!", "won't")
    False
    """
    raise_exercise_not_yet_started()


def find_word(haystack, needle):
    """
    #core - intermediate

    Find the word `needle` in the `haystack`. Return its position (start index).

    If the word is not found, return -1.

    >>> find_word("Where we're going, we don't need roads!", "do")
    22

    >>> find_word("Something else", "do")
    -1
    """
    raise_exercise_not_yet_started()


def fetch_vowels(given):
    """
    #core - intermediate

    Return a list of all ASCII vowels (a, e, i, o, u) in the given string.

    >>> fetch_vowels("Where we're going, we don't need roads!")
    ["e", "e", "e", "e", "o", "i", "e", "o", "e", "e", "o", "a"]
    """
    raise_exercise_not_yet_started()


def check_for_date(given):
    """
    #core - intermediate

    Check if the given string contains a date formatted as: YYYY-MM-DD.
    Directly return the match object produced by re.

    >>> check_for_date("Where we're going, we don't need roads!")
    None

    >>> check_for_date("Due date: 2025-07-03")
    <re.Match object; span=(10, 20), match='2025-07-03'>
    """
    raise_exercise_not_yet_started()


def count_animals(given):
    """
    #core - expert

    Return how often any of the following animal names appears in the given string:
    "cat", "dog", "donkey", "goose"

    >>> count_animals("Where we're going, we don't need roads!")
    0

    >>> count_animals("I have a cat, a dog, and a dogdonkey!")
    4
    """
    animals_to_find = ["cat", "dog", "donkey", "goose"]
    raise_exercise_not_yet_started()


def check_for_pattern(given):
    """
    #extra credit - intermediate

    Check if the given string contains the following pattern:
    Three spaces, followed by a 2–5 letter word, followed by at least one colon.

    >>> check_for_pattern("This doesn't contain it.")
    False

    >>> check_for_pattern("But this   does:!")
    True
    """
    raise_exercise_not_yet_started()


def contains_as_word(haystack, needle):
    """
    #extra credit - expert

    Check if the word `needle` appears in the `haystack` as a word.
    That means:
    - It appears in the string.
    - Before and after it are at least one character that are not letters.

    Return a bool.

    >>> contains_as_word("Where we're going, we don't need roads!", "need")
    True

    >>> contains_as_word("Where we're going, we don't need roads!", "going")
    True

    >>> contains_as_word("Where we're going, we don't need roads!", "do")
    False
    """
    raise_exercise_not_yet_started()


def find_most_common_name(name_list):
    """
    #extra credit - expert

    You are given a document that contains a list of names.
    Return which of the following occurs most often:
    "Lisa", "Laura", "Layla", "Larissa", "Lara"

    If none of them appears, return "".

    >>> find_most_common_name("")
    ""

    >>> find_most_common_name("Lisa Frey, Lisa Maurer; Laura Mung... Lara F.")
    "Lisa"
    """
    names_to_count = ["Lisa", "Laura", "Layla", "Larissa", "Lara"]
    raise_exercise_not_yet_started()
