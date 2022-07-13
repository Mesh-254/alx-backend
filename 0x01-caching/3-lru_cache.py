#!/usr/bin/python3
"""
Least Recently Used Cache module
"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """LRU cache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.cache_data_list = []
        self.counter = 0
   


    def put(self, key, item):
        """Add an item in the cache"""
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            value = self.cache_data_list.pop(0)
            del self.cache_data[value]
            print(f'DISCARD: {value}')

        if key is not None and item is not None:
            self.cache_data_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None:
            return self.cache_data.get(key)
        return None