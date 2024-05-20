#!/usr/bin/env python3
"""
1-simple_pagination.py
"""

from typing import Tuple, List, Dict
import csv
import math
index_range = __import__('0-simple_helper_function').index_range


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
        """get page by page number and size
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(dataset):
            return []
        else:
            if end >= len(dataset):
                end = len(dataset) - 1
            return dataset[start:end]

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        get index if data deleted
        """
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        if index is None:
            index = 0

        assert 0 <= index < len(dataset), "Index out of range."

        start_index = index
        end_index = min(index + page_size, len(dataset))
        data = dataset[start_index:end_index]

        if end_index == len(dataset):
            next_index = None
        else:
            next_index = end_index

        return {
            "index": start_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
            "total_pages": total_pages,
        }
