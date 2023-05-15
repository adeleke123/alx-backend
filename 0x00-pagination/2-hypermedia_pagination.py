#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page, page_size):
    """
    Calculates the start and end indexes for pagination.
    Args:
        page (int): The page number.
        page_size (int): The number of rows per page
    Returns:
        tuple: A tuple containing the start and end indexes.
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return start_idx, end_idx  # Returns a tuple (the start and end indexes)


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Gets hypermedia pagination information for a specific page.

        Args:
            page (int, optional): Page number (1-indexed). Defaults to 1.
            page_size (int, optional): Size of each page. Defaults to 10.

        Returns:
            dict: A dictionary containing the following key-value pairs:
              page_size: length of the returned dataset page
              page: current page number
              data: dataset page
              next_page: number of the next page, None if no next page
              prev_page: number of the previous page, None if no previous page
              total_pages (int): total number of pages in the dataset
        """
        # Get the total number of pages
        total_pages = math.ceil(len(self.dataset()) / page_size)

        # Get the dataset page
        data = self.get_page(page, page_size)

        # Calculate the next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
