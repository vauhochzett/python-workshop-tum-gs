class MockOpen:
    """
    A simple mockfile object that should be used and behave like the native open function.
    with MockOpen('dummy.txt') as f:
    >>> for line in f: print(line)
    Where 'dummy.txt' needs to be one of the supported mock files.

    instead
    >>> with open('dummy.txt') as f:
    >>> for line in f:
    >>> print(line)

    Where dummy.txt would need to be a real file.

    """

    def __init__(self, filename):
        all_data = {"dummy.txt": """a
b
c
d"""}
        if filename not in all_data:
            raise FileNotFoundError(
                "This is just a simple mock. It does not know anything about file '{}'".format(filename))
        self.rows = all_data[filename].split("\n")

    def __iter__(self):
        for i in self.rows:
            yield i

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


if __name__ == "__main__":
    with MockOpen("dummy.txt") as f:
        for line in f:
            print(line)
