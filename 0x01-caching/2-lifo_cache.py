#!/usr/bin/python3
""" BaseCaching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.order = []  # List to keep track of the order of keys

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key and item):
            self.cache_data[key] = item
            self.order.append(key)

            # If cache exceeds max items, discard the first item (FIFO)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()  # Remove the oldest key
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
