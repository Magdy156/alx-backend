#!/usr/bin/env python3
""" 1- FIFO
"""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cashing system"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign the value to the key"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstKey, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {firstKey}")

    def get(self, key):
        """Return the key value"""
        return self.cache_data.get(key)
