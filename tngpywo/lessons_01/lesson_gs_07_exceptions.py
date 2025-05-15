"""
The idea behind this lesson is to provide you examples for the most common exceptions that occur during Python coding.
Try to find out what every function tries to do and why it fails, and then fix it.

#extra credit - expert
"""


from tngpywo import raise_exercise_not_yet_started


def demo_index_error():
    """
    #core - easy

    Try to find out what the function tries to do and why it fails, and then fix it.
    """

    data = ["This", "is", "a", "sentence"]
    return [data[index] for index in [1, 2, 3, 4]]


def get_element_from_list(a_list, index):
    """
    #core - easy

    Return the element at position `index` in `list`.
    Return "Invalid!" if an IndexError is thrown.

    >>> get_element_from_list([1, 2, 3, 4], 2)
    3

    >>> get_element_from_list([1, 2, 3, 4], 6)
    Invalid!
    """
    raise_exercise_not_yet_started()


def validate_age(age):
    """
    #core - easy

    Raise a ValueError if age is negative.
    Otherwise return True.

    >>> validate_age(25)
    True
    >>> validate_age(-5)
    Traceback (most recent call last):
    ...
    ValueError: Age cannot be negative
    """
    raise_exercise_not_yet_started()


def safe_divide(a, b):
    """
    #core - easy

    Return the result of a divided by b.
    Handle division by zero by returning 0 in that case.

    >>> safe_divide(10, 2)
    5.0
    >>> safe_divide(5, 0)
    0
    """
    raise_exercise_not_yet_started()


def read_file_contents(filename):
    """
    #core - intermediate

    Return the contents of the specified file as a string.
    If the file doesn't exist, return an empty string.

    >>> read_file_contents("existing_file.txt")
    "file contents"
    >>> read_file_contents("nonexistent_file.txt")
    ""
    """
    raise_exercise_not_yet_started()


def demo_name_error():
    """
    #core - easy

    Try to find out what the function tries to do and why it fails, and then fix it.
    """

    def doubled(number):
        return number * 2
    return double(17)


def demo_type_error(my_integer, my_string):
    """
    #core - easy

    Try to find out what the function tries to do and why it fails, and then fix it.
    """
    return my_integer + my_string


def demo_key_error():
    """
    #extra credit - intermediate

    Try to find out what the function tries to do and why it fails, and then fix it.
    """
    return {f"key {k}": k * 2 for k in range(100)}["key8"]


def demo_value_error():
    """
    #extra credit - difficult

    Try to find out what the function tries to do and why it fails, and then fix it.
    """
    s = "a:1;b:22;c:-2;q:4;k;w:5"
    pairs = s.split(";")
    return {k: v for k, v in [p.split(":") for p in pairs]}
