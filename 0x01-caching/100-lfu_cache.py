#!/usr/bin/python3
""" BaseCaching module
"""
from collections import defaultdict, OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class
    Inherits from BaseCaching and implements a basic LFU caching system.
    """

    def __init__(self):
        """ Initialize the BasicCache instance
        """
        super().__init__()
        # Dictionary to track usage frequency
        self.usage_frequency = defaultdict(int)
        # Ordered dictionary to group items by frequency
        self.frequency_ordered_cache = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache
        If the cache exceeds the maximum allowed items,
        discard the least frequently used item (LFU).
        """
        if key and item:
            # If the key already exists, update its frequency
            if key in self.cache_data:
                self.usage_frequency[key] += 1
            else:
                self.usage_frequency[key] = 1

            # Add the item to the cache
            self.cache_data[key] = item

            # Update the frequency-ordered cache
            self._update_frequency_ordered_cache(key)

            # discard the least frequently used item (LFU)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self._discard_least_frequent_item()

    def get(self, key):
        """ Get an item by key
        Return the value in self.cache_data linked to key,
        or None if key is None or not in cache.
        """
        if key in self.cache_data:
            # Update the usage frequency
            self.usage_frequency[key] += 1

            # Update the frequency-ordered cache
            self._update_frequency_ordered_cache(key)

            return self.cache_data[key]
        return None

    def _update_frequency_ordered_cache(self, key):
        """ Update the frequency-ordered cache
        after an item is accessed or added
        """
        frequency = self.usage_frequency[key]
        if frequency in self.frequency_ordered_cache:
            self.frequency_ordered_cache[frequency].remove(key)
            if not self.frequency_ordered_cache[frequency]:
                del self.frequency_ordered_cache[frequency]
        self.frequency_ordered_cache[frequency] = OrderedDict(
            sorted(self.frequency_ordered_cache.get(frequency, {}).items(),
                   key=lambda x: x[1])
        )
        self.frequency_ordered_cache[frequency][key] = None

    def _discard_least_frequent_item(self):
        """ Discard the least frequently used item (LFU)
        If multiple items have the same lowest frequency,
        use the LRU algorithm to select the item.
        """
        min_frequency = next(iter(self.frequency_ordered_cache))
        least_frequent_items = self.frequency_ordered_cache[min_frequency]

        # Find the least recently used item
        lru_key = next(iter(least_frequent_items))

        # Remove the item from all data structures
        del self.cache_data[lru_key]
        del self.usage_frequency[lru_key]
        least_frequent_items.popitem(last=False)

        print(f"DISCARD: {lru_key}")
