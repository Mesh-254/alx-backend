#!/usr/bin/env python3
""" fifo caching module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """Add an item in the cache"""

        if key is None and item is None:
            return None
        if len(self.cache_data) >= self.MAX_ITEMS:
            first_item = self.cache_data_list.pop(0)
            del self.cache_data[first_item]
            print("DISCARD: {}".format(first_item))
        self.cache_data[key] = item
        self.cache_data_list.append(key)

    def get(self, key):
        """Get an item by key"""

        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None