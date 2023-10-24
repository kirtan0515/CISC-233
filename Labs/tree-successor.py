import random


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Insert nodes
r = Node(50)
nodes = [30, 20, 40, 70, 60, 80]
for x in nodes:
    insert(r, Node(x))

# Print in ascending order
print("Inorder traversal:")
inorder = inorder(r, [])
for x in inorder:
    print(x.val)

# Print min
print("Minimum:", tree_min(r).val)

# Print max
print("Maximum:", tree_max(r).val)

# Check if key exists
if search(r, 2):
    print("2 exists in tree")
else:
    print("2 does not exist in tree")

# Print successor
print("Successor of 29:", successor(r, 29).val)