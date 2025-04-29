#!/usr/bin/env python3
"""
Implement a get_hyper method
"""
import math
import csv
from typing import Dict, List


def index_range(page: int, page_size: int) -> tuple:
    """
    Write a function named index_range that takes two integer arguments.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


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
        Get a page from the dataset
        """
        assert (isinstance(page, int) and page > 0), \
            "page must be a positive integer"
        assert (isinstance(page_size, int) and page_size > 0), \
            "page_size must be a positive integer"

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns pagination data with hypermedia metadata
        """
        data = self.get_page(page, page_size)
        total = len(self.dataset())
        total_pages = math.ceil(total / page_size) if page_size else 0

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
