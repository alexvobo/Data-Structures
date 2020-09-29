from LinkedList import LinkedList
import random

NOT_FOUND = "ITEM {} NOT FOUND"


class HashTable:
    def __init__(self, size=10):
        self.hashtable = {}  # this contain our keys and values
        self.tablesize = size
        self.indices = []

    def hash_func(self, key):
        return key % self.tablesize

    def insert(self, item=None, index=False):
        # We are going to hash the item, then load it into table. Check if key already exists.
        # Key doesnt exist > just create LL
        if item is not None:
            key = self.hash_func(item)
            # If an entry does not exist at that key we create a linked list there
            try:
                bucket = self.hashtable[key]
                bucket.insert(index, item) if index else bucket.append(item)
                # print("Added to existing bucket")
            except KeyError:
                self.hashtable[key] = []
                self.hashtable[key].append(item)
                # print("Created new bucket at ", key, "for item: ", item)
                #! TESTING
                self.indices.append(key)

    def delete(self, item=None, index=False):
        if item is not None:
            key = self.hash_func(item)
            try:
                bucket = self.hashtable[key]
                #! rework later currently getItem returns a tuple (pos, node), passes index of item to delete function
                removed = bucket.pop(index) if index else bucket.remove(item)
                if removed:
                    print([print(str(i) + "->") for i in bucket])
                    return removed
            except KeyError:
                print("Failed to delete")
        return False

    def get(self, item=None):
        if item is not None:
            key = self.hash_func(item)
            try:
                bucket = self.hashtable[key]
                if bucket:
                    #! rework later currently getItem returns a tuple (pos, node)
                    try:
                        index = bucket.index(item)
                        print("Found item: {} in bucket #{} index #{}".format(
                            item, key, index))
                        return index
                    except ValueError:
                        pass
            except KeyError:
                print("Bucket not found")

        print(NOT_FOUND.format(item))
        return False

    def printht(self):
        for k, v in self.hashtable.items():
            print("Bucket: ", k)
            txt = []
            for j in v:
                txt.append(j)
            print(str(txt))


''' Will shuffle a list, used for testing linked list functions'''


def randomly(listseq):
    shuffled = listseq
    random.shuffle(shuffled)
    return iter(shuffled)


ht = HashTable(50)
items = []
for i in range(100):
    # ht.insert(i)
    ht.insert(random.randint(0, 100))


ht.printht()

print("-----REMOVING-----")
for idx in ht.indices:
    items = ht.hashtable[idx].copy()
    print('actual', items)
    randomly(items)
    print('shuffled', items)
    if items:
        for it in items:
            ht.get(it)
            ht.delete(it)
        items = []
    print('---')
ht.printht()
