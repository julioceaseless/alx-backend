#!/usr/bin/env python3
"""
Create an LFU cache with LRU tie-breaker
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Least Frequently Used caching class with LRU tie-breaker
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        # Frequency count for each key
        self.freq = {}

        # Order of usage for each frequency
        self.usage = {}

        # Overall access order to handle LRU within same frequency
        self.access_order = []

    def _update_usage(self, key):
        """
        Update the usage order of a key
        """
        freq = self.freq[key]
        self.usage[freq].remove(key)
        if not self.usage[freq]:
            del self.usage[freq]

        self.freq[key] += 1
        freq = self.freq[key]
        if freq not in self.usage:
            self.usage[freq] = []
        self.usage[freq].append(key)

        # Update the access order to move the key to the end (MRU)
        self.access_order.remove(key)
        self.access_order.append(key)

    def put(self, key, item):
        """
        Add data to cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self._update_usage(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the LFU key(s)
                    min_freq = min(self.usage.keys())
                    lfu_keys = self.usage[min_freq]

                    # If there's more than one LFU key, remove LRU
                    if len(lfu_keys) > 1:
                        lru_key = next(k for k in self.access_order if k in lfu_keys)
                    else:
                        lru_key = lfu_keys[0]

                    # Remove the selected key
                    self.cache_data.pop(lru_key)
                    self.freq.pop(lru_key)
                    self.usage[min_freq].remove(lru_key)
                    if not self.usage[min_freq]:
                        del self.usage[min_freq]
                    self.access_order.remove(lru_key)
                    print("DISCARD: {}".format(lru_key))

                # Add new item
                self.cache_data[key] = item
                self.freq[key] = 1
                if 1 not in self.usage:
                    self.usage[1] = []
                self.usage[1].append(key)
                self.access_order.append(key)

    def get(self, key):
        """
        Get data from cache
        """
        if key in self.cache_data:
            self._update_usage(key)
            return self.cache_data[key]
        return None
