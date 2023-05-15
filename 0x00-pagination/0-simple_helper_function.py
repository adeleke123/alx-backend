#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    Calculates the start and end indexes for pagination.

    Args:
        page (int): The page number.
        page_size (int): The number of rows per page

    Returns:
        tuple: A tuple containing the start and end indexes.
    """
    # Calculate the start index based on the page number and page size
    start_idx = (page - 1) * page_size

    # Calculate the end index by adding the start index to the page size
    end_idx = start_idx + page_size

    # Return a tuple containing the start and end indexes
    return start_idx, end_idx
