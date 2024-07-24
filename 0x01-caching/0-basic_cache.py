#!/usr/bin/env python3
""" 0- basic
"""


from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """basic cashing system"""

    def put(self, key, item):
        """Assign the value to the key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the key value"""
        return self.cache_data.get(key)
