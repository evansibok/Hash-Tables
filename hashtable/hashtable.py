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
        self.storage = [None] * capacity

    """
    The core of the FNV-1 hash algorithm is as follows:
        hash = offset_basis
        for each octet_of_data to be hashed
            hash = hash * FNV_prime
            hash = hash xor octet_of_data
        return hash
    -----------------------------------------------------------
    hash: n bit unsigned integer, where n is bit length of hash

    The multiplication is performed modulo 2^n where n is bit length of hash

    The xor is performed on the low order octect (8 bits) of hash

    The FNV_prime is dependent on n, the size of the hash:
        32 bit FNV_prime = 224 + 28 + 0x93 = 16777619
        64 bit FNV_prime = 240 + 28 + 0xb3 = 1099511628211
    Part of the magic of FNV is the selection of the FNV_prime for a given sized unsigned integer. Some primes do hash better than other primes for a given integer size.

    The offset_bases for FNV-1 is dependent on n, the size of the hash:
        32 bit offset_basis = 2166136261
        64 bit offset_basis = 14695981039346656037
    """

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    """
    DJB2 Algorithm

    hash = 0;
    for (each character)
        hash = (hash * 33) + (the character); 
        // or 
        // hash = (((hash << 5) + (the character)) + (the character))
    hash_index = hash & ((some power of two) - 1);
    """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            # get the unicode point of the character and hash
            hashed = ((hash << 5) + hash) + ord(c)
        return hashed

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
        index = self.hash_index(key)
        self.storage[index] = value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if not key:
            return None

        index = self.hash_index(key)
        return self.storage[index]

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # double capacity size
        self.storage = self.storage * 2


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
