#!/usr/bin/python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class that represents a caching system using the FIFO algorithm"""

    def __init__(self):
        """Initializes the FIFOCache"""
        super().__init__()

    def put(self, key, item):
        """Gives the item value to the key in the cache using the FIFO algo
        Args:
            key: The key to assign the item value to.
            item: The value to be assigned to the key.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the first item (FIFO)
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            self.cache_data[key] = item

    def get(self, key):
        """Returns the value associated with the key in the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key,
            or None if the key is None / doesn't exist in the cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
