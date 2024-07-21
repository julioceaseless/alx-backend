#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) ->tuple:
    """
    Determines the start and end index based on the pagination
    parameters
    """
    end_index = page_size * page
    start_index = end_index - page_size
    return (start_index, end_index)

