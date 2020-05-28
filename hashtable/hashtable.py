class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity  # Storage bucket

    def __repr__(self):
        return f"capacity: {self.capacity}, storage: {self.storage}"

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        pass

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.

        *** DJB2 Algorithm ***
        hash = 5381
        for character in string/key:
            hashed = (hash * 33) + ord(character)
            or
            // Optimized version of the one above
            hashed = ((hash << 5) + hash) + ord(character)
            return hashed
        """
        hash = 5381
        for c in key:
            hash = ((hash << 5) + hash) + ord(c)
            # hash &= 0x7F
            return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # WITHOUT COLLISION
        index = self.hash_index(key)
        if self.storage[index] != None:
            print(
                f"Collision! Overwriting from '{self.storage[index]}' to '{value}'")
        self.storage[index] = value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # WITHOUT COLLISION
        index = self.hash_index(key)
        self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # WITHOUT COLLISION
        if not key:
            return None
        else:
            index = self.hash_index(key)
            return self.storage[index]

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        pass


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("firefox", "this is firefox")
    hi = ht.hash_index("firefox")
    print("fox djb2", ht.djb2("firefox"))
    print('fox i', hi)
    print("")

    ht.put("edge", "this is edge")
    hi = ht.hash_index("edge")
    print("edge djb2", ht.djb2("edge"))
    print('edge i', hi)
    print("")

    ht.put("brave", "this is brave")
    hi = ht.hash_index("brave")
    print("brave djb2", ht.djb2("brave"))
    print('brave i', hi)
    print("")

    print('ht', ht)
    print("")

    # Test storing beyond capacity
    print('fox get', ht.get("firefox"))
    print('edge get', ht.get("edge"))
    print('brave', ht.get("brave"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print('fox get', ht.get("firefox"))
    print('edge get', ht.get("edge"))
    print('brave', ht.get("brave"))

    print("")
