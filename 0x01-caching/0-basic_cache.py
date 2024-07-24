#!/usr/bin/env python3
"""
Basic caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching
    """
    def put(self, key, item):
        """
        Add data to cache
        """
        if key and item:
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
