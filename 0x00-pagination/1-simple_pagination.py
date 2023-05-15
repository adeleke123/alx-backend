#!/usr/bin/env python3
"""
Simple pagination
"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Finds the correct indexes to paginate the dataset.

        Args:
            page (int, optional): Page number (1-indexed). Defaults to 1.
            page_size (int, optional): Size of each page. Defaults to 10.

        Returns:
            list: A list of rows from the dataset.
        """
        # Page and Page_size must be an interger that is greater than 0
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        data_size = len(self.dataset())
        start_idx, end_idx = index_range(page, page_size)
        end_idx = min(end_idx, data_size)

        # Return empty list if start index is out of range
        if start_idx >= data_size:
            return []

        return self.dataset()[start_idx:end_idx]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indexes for pagination.
    Args:
        page (int): The page number.
        page_size (int): The number of rows per page
    Returns:
        tuple: A tuple containing the start and end indexes.
    """
    return ((page - 1) * page_size, page * page_size)
