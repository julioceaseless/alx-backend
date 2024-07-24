#!/usr/bin/env python3
"""
Create a FIFO cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching class
    """
    def __init__(self):
        """
        initialize instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Add data to cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                cache_keys = list(self.cache_data.keys())
                popped_data = self.cache_data.pop(cache_keys[0])
                print("DISCARD: {}".format(cache_keys.pop(0)))
        else:
            pass

    def get(self, key):
        """
        Get data from cache
        """
        if key:
            return self.cache_data.get(key)
        return None
