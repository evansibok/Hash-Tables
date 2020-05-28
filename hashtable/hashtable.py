class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"key: {self.key}, value: {self.value}"


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
            hash &= 0x7FFFFFFF
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
        # index = self.hash_index(key)
        # if self.storage[index] != None:
        #     print(
        #         f"Collision! Overwriting from '{self.storage[index]}' to '{value}'")
        # self.storage[index] = value

        # WITH COLLISION
        index = self.hash_index(key)
        node = HashTableEntry(key, value)

        # Handle when the index is empty
        # if storage index is empty:
        if not self.storage[index]:
            # -> Add the node
            self.storage[index] = node

        # if the index is not empty
        else:
            # get the current node
            cur_node = self.storage[index]
            # while the current node's next is not empty
            while cur_node:
                # Handle when the key already exists (overwrite the value)
                if cur_node.key == key:
                    cur_node.value = value
                    break
                # Handle when the key doesn't exist (add the new node)
                if cur_node.next:
                    cur_node = cur_node.next
                else:
                    cur_node.next = node

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # WITHOUT COLLISION
        # if not key:
        #     return
        # else:
        #     index = self.hash_index(key)
        #     self.storage[index] = None
        pass

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # # WITHOUT COLLISION
        # if not key:
        #     return None
        # else:
        #     index = self.hash_index(key)
        #     return self.storage[index]

        index = self.hash_index(key)
        # Handle when index is empty
        if not self.storage[index]:
            return None

        # If index is not empty
        # Let's move through the node while there's a next node
        cur_node = self.storage[index]
        while cur_node:
            # cur_node = cur_node.next
            # Handle when the key is found
            if key == cur_node.key:
                # -> return the value
                return cur_node.value
            elif cur_node.next != None:
                # keep moving through the nodes
                cur_node = cur_node.next
            # if the key is not found
            else:
                # -> return f"{key} not found!"
                return f"{key} not found!"

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # number_of_entries = ?
        # storage_size = self.capacity
        # lf = number_of_entries / storage_size
        # if lf > 0.7:
        # Double the storage by 2
        # elif lf < 0.2:
        # Reduce the storage size by 2
        # else:
        # return
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
    print('brave get', ht.get("brave"))

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
