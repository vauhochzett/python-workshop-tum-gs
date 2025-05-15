from tngpywo import raise_exercise_not_yet_started


def add(a, b):
    """
    #core - easy

    Return the sum of `a` and `b`.

    >>> add(1, 2)
    3

    >>> add(-1, 1)
    0
    """
    raise_exercise_not_yet_started()


def outer(a, b):
    """
    #core - intermediate

    Call the `add` function from this function and return the result

    >>> outer(2, 3)
    5
    """
    raise_exercise_not_yet_started()


# #core - intermediate
#
# Create a function subtract(a, b) that returns the result of
# subtracting b from a.
# >>> subtract(5, 3)
# 2
#
raise_exercise_not_yet_started()


def apply_twice(func, arg):
    """
    #core - intermediate

    Apply the given function to the argument twice.

    >>> def add_one(x):
    ...     return x + 1
    >>> apply_twice(add_one, 5)
    7
    """
    raise_exercise_not_yet_started()


# #core - intermediate
#
# Create a function handle(cmd, left, right) that applies a command to
# the two parameters 'left' and 'right'.
#
# - If the command is "add", it returns the value of add(left, right)
# - For "subtract", the same with subtract(left, right)
# - If there is any other command given, it returns "ERROR!"
#
# >>> handle("add", 12, -12)
# 0
#
# >>> handle("subtract", -12, -12)
# 0
#
# >>> handle("multiply", 1, 0)
# "ERROR!"
#
raise_exercise_not_yet_started()


def create_adder(addend):
    """
    #extra credit - expert

    Return a function named `adder` that adds `addend` to its argument.

    >>> add_three = create_adder(3)
    >>> add_three(5)
    8
    """
    return adder


def create_greeter(greeting):
    """
    #extra credit - expert

    Return a function that takes a name and returns a greeting string.

    >>> hello = create_greeter("Hello")
    >>> hello("Alice")
    "Hello, Alice!"
    >>> hi = create_greeter("Hi")
    >>> hi("Bob")
    "Hi, Bob!"
    """
    raise_exercise_not_yet_started()


def create_incrementor(target, key):
    """
    #extra credit - expert

    Return a function that

    - Expects one argument `increment`
    - Adds the value of `increment` to `target[key]`.
    - Returns `target`.

    Expect `target` to be a dict that already contains "key".

    >>> i = create_incrementor({"x" : 1}, "x")
    >>> i(5)
    {"x": 6}
    """
    raise_exercise_not_yet_started()
