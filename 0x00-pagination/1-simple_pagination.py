#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ initialize """
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
        Determines the start and end index based on the pagination
        parameters
        """
        assert type(page) == int
        assert (page > 0)
        assert type(page_size) == int
        assert (page_size > 0)

        # determine the end index
        end_index = page_size * page

        # determine the start index
        start_index = end_index - page_size

        # return empty list if the indexes are out of range of the dataset
        if end_index > len(self.dataset()):
            return []

        data = self.dataset()
        return data[start_index:end_index]
