#!/usr/bin/env python3
"""
Create a FIFO cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Last In First Out caching class
    """
    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add data to cache
        """
        # Add item to cache
        if key and item:
            if key in self.cache_data:
                # Update the existing item and move the key to the end
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # remove the least recently used key
                lru_key = self.order.pop(0)

                popped_item = self.cache_data.pop(lru_key)

                print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get data from cache
        """
        if key and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
