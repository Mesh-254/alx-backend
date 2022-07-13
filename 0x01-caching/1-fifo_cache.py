#!/usr/bin/python3
"""
FIFO Cache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - a FIFO cache system
      - a max_items constant
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None and item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            value = self.cache_data_list.pop(0)
            self.cache_data.pop(value)
            print(f'DISCARD: {value}')

        self.cache_data_list.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
