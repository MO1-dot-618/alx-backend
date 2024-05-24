#!/usr/bin/python3
""" BaseCaching module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key and item):
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            # Move the key to the end to mark it as recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
