#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that represents a caching system."""

    def put(self, key, item):
        """Assigns the item value to the key in the cache.

        Args:
            key: The key to assign the item value to.
            item: The value to be assigned to the key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value associated with the key in the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or
            None if the key is None / doesn't exist in the cache.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
