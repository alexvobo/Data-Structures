from LinkedList import LinkedList
import random
import sys
import io


class HashTable:
    def __init__(self, size=10):
        self.hashtable = {}  # this contain our keys and values
        self.tablesize = size
        self.indices = []

    def hash_func(self, key):
        return key % self.tablesize

    def insert(self, item):
        # We are going to hash the item, then load it into table. Check if key already exists.
        # Key exists > chain
        # Key doesnt exist > just create LL

        key = self.hash_func(item)
        # If an entry does not exist at that key we create a linked list there
        try:
            bucket = self.hashtable[key]
            bucket.add(item)
            #print("Added to existing bucket")
        except KeyError:
            self.hashtable[key] = LinkedList()
            self.hashtable[key].add(item)
            #print("Created new bucket at ", key, "for item: ", item)
            #! TESTING
            self.indices.append(key)

    def delete(self, item):
        key = self.hash_func(item)
        try:
            bucket = self.hashtable[key]
            #! rework later currently getItem returns a tuple (pos, node), passes index of item to delete function
            removed = bucket.removeItem(item)
            if removed:
                bucket.printListString()
                return removed
        except KeyError:
            print("Failed to delete")
        return False

    def get(self, item):
        key = self.hash_func(item)

        bucket = self.hashtable[key]
        if bucket:
            #! rework later currently getItem returns a tuple (pos, node)
            ret_item = bucket.getItem(item)[1]
            print("Found item: {} in bucket #{}".format(item, key))
            return ret_item

        return False

    def printht(self):
        for k, v in self.hashtable.items():
            print("Bucket: ", k)
            txt = []
            for j in iter(v):
                txt.append(j.data)
            print(str(txt))


''' Will shuffle a list, used for testing linked list functions'''


def randomly(listseq):
    shuffled = listseq
    random.shuffle(shuffled)
    return iter(shuffled)

#! TESTING PURPOSES ONLY, SUPPRESSES OUTPUT
# text_trap = io.StringIO()
# sys.stdout = text_trap
ht = HashTable(50)
items = []
for i in range(100):
    #ht.insert(i)
    ht.insert(random.randint(0, 100))


ht.printht()

print("-----REMOVING-----")
for idx in ht.indices:
    for it in iter(ht.hashtable[idx]):
        items.append(it.data)
    print('actual', items)
    randomly(items)
    print('shuffled', items)
    if items:
        for it in items:
            # ht.get(it)
            ht.delete(it)
        items = []
    print('---')
ht.printht()
