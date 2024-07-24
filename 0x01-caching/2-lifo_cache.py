#!/usr/bin/env python3
""" 2- LIFO
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cashing system"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign the value to the key"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lastKey, _ = self.cache_data.popitem()
                print(f"DISCARD: {lastKey}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Return the key value"""
        return self.cache_data.get(key)
