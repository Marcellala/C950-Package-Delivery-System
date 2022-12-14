# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=41):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Getter to create hash key
    def getter(self, key):
        bucket = int(key) % len(self.table)
        return bucket

    # Inserts a new item into the hash table.
    # Time Complexity: 0(1)
    # Space Complexity: O(n)
    def insert(self, key, item):
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it exists
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        # if the key doesn't exist, insert the item
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

        # insert the item to the end of the bucket list.
        bucket_list.append(item)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def lookup(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return None

    # Removes an item with matching key from the hash table
    # Time Complexity: 0(1)
    # Space Complexity: O(n)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])



