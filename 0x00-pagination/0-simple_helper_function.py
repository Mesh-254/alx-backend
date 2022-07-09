#!/usr/bin/env python3
"""Function named index_range that takes two integer
arguments page and page_size and
returns a tuple containing start index and end index """


def index_range(page, page_size):
    """
    Returns a tuple containing start index and end index
    """
    return (page - 1) * page_size, page * page_size
