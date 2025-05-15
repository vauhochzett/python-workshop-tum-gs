"""

# Getting started

## Install uv

Follow the instructions on: https://docs.astral.sh/uv/getting-started/installation/

## Initialize uv

* Navigate to the directory in your terminal
* Execute `uv sync`


# Setting up the tests

## Select the Python interpreter installed by uv

* The Python interpreter in your IDE should be: .venv/bin/python
    * With the keyboard: Ctrl-Shift-P -> "Python: Select Interpreter"
    * In the GUI: Help -> Show all commands -> dto.

## Open the tests

* Open the test explorer (the flask in the left column)
* Navigate to `.../tngpywo/tests/lessons_01`
* Run `test_lesson_01_getting_started.py`


# Starting on the exercises

Now you're set up to start! Your goal is to make the tests "green" (succeed).

Exercises are categorized into "core" and "extra credit" to guide your focus; core
exercises are essential for understanding the workshop material, while extra credit
exercises are optional challenges for those who wish to dive deeper.

In addition, an estimated level of difficulty (easy, intermediate, expert) is given.
"""


from tngpywo import raise_exercise_not_yet_started


# Example:
def version():
    """
    Return the version string of our project. Currently, this is 'tng_0.0.2'.

    >>> version()
    'tng_0.0.2'
    """

    # This is how you return a value:
    return "tng_0.0.2"


def working_with_variables():
    """
    #core - easy

    Return the value of y multiplied by 10.

    >>> working_with_variables()
    500
    """
    # Do not modify this line!
    y = 50

    # Your solution must be below this line
    raise_exercise_not_yet_started()


def your_first_calculation(x):
    """
    #core - easy

    Return the value of (two times (`x` to the power of three)) minus five.

    >>> your_first_calculation(100)
    1999995
    """
    raise_exercise_not_yet_started()


def floating_around(x):
    """
    #core - easy

    Test if `x` divided by 2 is smaller than 5.5

    >>> floating_around(10)
    True

    >>> floating_around(29)
    False
    """
    raise_exercise_not_yet_started()


def insert_into_string(value):
    """
    #core - intermediate

    Return a string that inserts the given value in the middle:

    >>> convert_to_string(5)
    "I have 5 sheep"

    >>> convert_to_string("cinque")
    "I have cinque sheep"
    """
    raise_exercise_not_yet_started()


def join_arguments(a, b, separator="-"):
    """
    #core - intermediate

    Return a joined string of the two parameters `a` and `b`.

     >>> join_arguments('first', 'second')
     'first-second'

     >>> join_arguments('x', 5, ',')
     'x,5'
    """
    raise_exercise_not_yet_started()


def is_float(value):
    """
    #core - intermediate

    Test if the given value is of type `float`

     >>> is_float(5)
     False

     >>> is_float(5.0)
     True
    """
    raise_exercise_not_yet_started()


def is_number(value):
    """
    #extra credit - intermediate

    Test if the given value is any number type.

     >>> is_number(5)
     True

     >>> is_number(5.0)
     True

     >>> is_number("5.0")
     False
    """
    raise_exercise_not_yet_started()


def xor(left, right):
    """
    #extra credit - expert

    Implement an xor between `left` and `right` using only logical operators

     >>> xor(True, True)
     False

     >>> xor(True, False)
     True

     >>> xor(False, False)
     False
    """
    raise_exercise_not_yet_started()


if __name__ == "__main__":
    print(__doc__)
    print(f"Version returned: {version()!r}")
