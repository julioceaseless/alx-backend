#!/usr/bin/env python3
"""
Create a FIFO cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Last In First Out caching class
    """
    def __init__(self):
        """
        initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Add data to cache
        """
        # Add item to cache
        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                cache_keys = list(self.cache_data.keys())

                # remove the most recent addition
                latest_key = cache_keys.pop()

                popped_item = self.cache_data.pop(latest_key)

                print("DISCARD: {}"
                      .format(latest_key))

            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """
        Get data from cache
        """
        if key:
            return self.cache_data.get(key)
        return None
