import traversal as trav
NOT_FOUND = "ITEM -{}- NOT FOUND"
FOUND = "ITEM -{}- FOUND"

output = []


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, item):
        # If current node has no data, it will fill the node.

        if self.data is not None:
            # If the item is smaller than the current node's item, we will move it to the left subtree
            if item < self.data:
                if self.left is None:
                    self.left = Node(item)
                else:
                    self.left.insert(item)
            # If the item is smaller than the current node's item, we will move it to the left subtree
            elif item > self.data:
                if self.right is None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)
            # If the item is equal to the current item do nothing because duplicates are not allowed.
        else:
            self.data = item

    def get(self, item):
        if self.data is not None and item is not None:
            if item < self.data:
                if self.left is not None:
                    return self.left.get(item)
                else:
                    print(NOT_FOUND.format(item))
            elif item > self.data:
                if self.right is not None:
                    return self.right.get(item)
                else:
                    print(NOT_FOUND.format(item))
            else:
                print(FOUND.format(item))

    def printTree(self):
        if self.left is not None:
            self.left.printTree()
        print(self.data)
        if self.right is not None:
            self.right.printTree()


start = 5
tree_root = Node(start)
for i in range(1, 10):
    if i != start:
        tree_root.insert(i)
# tree_root.printTree()
print(trav.in_order(tree_root))
print(trav.pre_order(tree_root))
print(trav.post_order(tree_root))
