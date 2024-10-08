#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        # index the dataset
        if self.__indexed_dataset is None:
            dataset = self.dataset()

            # slice the first 1000 entries
            truncated_dataset = dataset[:1000]

            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(truncated_dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary containing the hypermedia
        pagination information."""
        data = self.indexed_dataset()
        start = 0 if index is None else index
        assert data is not None

        data_ = []
        current_index = start

        while len(data_) < page_size and current_index < len(data):
            item = data.get(current_index)
            if item is not None:
                data_.append(item)
            current_index += 1

        next_index = current_index if current_index < len(data) else None

        hyper_index_dict = {
            "index": start,
            "next_index": next_index,
            "page_size": len(data_),
            "data": data_,
        }

        return hyper_index_dict
    """
    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        assert index is not None and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        assert index < len(self.dataset())

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index
        next_index = index

        # Collect the data for the current page
        while len(data) < page_size and next_index < len(indexed_data):
            if next_index in indexed_data.keys():
                data.append(indexed_data.get(next_index))
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
    """
