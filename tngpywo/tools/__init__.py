#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

import tngpywo


def get_resource(resource):
    """
    A little helper to allow easy access to data files contained in this package.

    Note that `pkgutil.get_data <https://docs.python.org/3/library/pkgutil.html/>`_ would directly return the
    the actual file content. The only reason get_data is not used here, is for didactic reasons.

    >>> open(get_resource('data/NASA_access_log_Jul95_head5000.txt')).read(77)
    '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0"'

    :param resource: a filename of a file in the tngpywo package for example 'data/NASA_access_log_Jul95_head5000.txt'
    """
    d = os.path.dirname(sys.modules[tngpywo.__name__].__file__)
    return os.path.join(d, resource)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
