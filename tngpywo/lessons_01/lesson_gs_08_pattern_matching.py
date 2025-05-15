from tngpywo import raise_exercise_not_yet_started


def get_first_name(name: str):
    """
    #core - intermediate

    Split the first name from the given name with pattern matching.

    The given name can consist of:
    1. just a first name
    2. a first and last name
    3. a first, middle, and last name

    In all cases, return the first name only.

    >>> get_first_name("Adam")
    "Adam"

    >>> get_first_name("Mara Max")
    "Mara"

    >>> get_first_name("Sebas Gonzales Martines")
    "Sebas"
    """
    raise_exercise_not_yet_started()


def handle_command(cmd: str):
    """
    #core - expert

    Handle the given command with pattern matching.

    The command can be:
    - "shout" -> return "AAAAH!"
    - "count to <x>" -> return a list of values from 0 to x
    - "is <a> in <b> -> check if string a is in b

    Implement the functions _get_shouting(), _count_to(x), and _is_in(needle, haystack)
    below with the required functionality. Call them from this function.

    If the command is invalid, raise a ValueError.

    >>> handle_command("shout")
    "AAAAH!"

    >>> handle_command("count to 3")
    [1, 2, 3]

    >>> handle_command("is dog in doghouse")
    True

    >>> handle_command("typo")
    ValueError: could not parse command: typo
    """
    raise_exercise_not_yet_started()


def _get_shouting():
    raise_exercise_not_yet_started()


def _count_to(x):
    raise_exercise_not_yet_started()


def _is_in(needle, haystack):
    raise_exercise_not_yet_started()
