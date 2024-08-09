#!/usr/bin/env python3
"""Simple LRU cache"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()

        self.order = []

        # key = key, value = no of times the key is accessed
        self.freq = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                """overwrite the key"""
                self.cache_data[key] = item
                # Update trackers
                # reorder the key in the list
                self.order.remove(key)
                self.order.append(key)

                # increment frequency
                self.freq[key] = self.freq.get(key, 0) + 1

            else:
                """add a new key, value"""
                # check if buffer is full
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # get lease usage value
                    least_frequency = min(self.freq.values())

                    # store keys with same frequency
                    least_freq_keys = []
                    # add least used keys to list
                    least_freq_keys = [key
                                       for key, value in self.freq.items()
                                       if value == least_frequency]
                    """for key, value in self.freq.items():
                        if value == least_frequency:
                            least_freq_keys.append(key)
                    """
                    # if many keys, use LRU to pick the oldest
                    if len(least_freq_keys) > 1:
                        target_key = None
                        # iterate through the order list
                        for i in self.order:
                            if i in least_freq_keys:
                                target_key = i
                                break
                    else:
                        target_key = least_freq_keys[0]

                    # delete the key
                    del self.cache_data[target_key]
                    del self.freq[target_key]
                    self.order.remove(target_key)
                    print(f"DISCARD: {target_key}")

                """ add and track the new key """
                self.cache_data[key] = item
                # add to order list
                self.order.append(key)
                # add to key usage tracker
                self.freq[key] = 1

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            self.freq[key] = self.freq.get(key, 0) + 1
            return self.cache_data[key]
        return None
