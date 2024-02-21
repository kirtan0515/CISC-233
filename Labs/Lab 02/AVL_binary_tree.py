# Q- 2. (2.5 pts)
# In this question you will develop a Binary Search Tree class, you don’t have to worry about
# insertion, deletion, search, etc., the constructor of the BST class you accept a list and build the tree,
# in your class you need to have a method called AVL to check if the tree is balanced. An AVL tree is a binary search
# tree that is height balanced: for each node x , the heights of the left and right subtree of x differ by at most 1,
# you need to be clear about the balance factor of the node.
#
#                       Balance Factor = |hl − hr | = {−1, 0, 1} to check

# the correctness of your implementation use the following two lists:
# a. [20, 15, 10, 5, 8, 2] unbalanced
# b. [10, 5, 15, 2, 8, 20] balanced
import random


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Binary_Search_Tree:
    def __init__(self, keys):
        self.root = None
        for key in keys:
            self.insert(key)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.data:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def is_avl(self):
        is_balanced, _ = self._is_avl(self.root)
        return is_balanced

    def _is_avl(self, node):
        if node is None:
            return True, 0

        left_avl, left_height = self._is_avl(node.left)
        right_avl, right_height = self._is_avl(node.right)

        balance_factor = abs(left_height - right_height)

        if balance_factor > 1:
            return False, 0

        return left_avl and right_avl, max(left_height, right_height) + 1

    def get_height(self, key):
        return self._get_height(self.root, key)

    def _get_height(self, node, key):
        if node is None:
            return 0

        if key < node.data:
            return self._get_height(node.left, key) + 1
        elif key > node.data:
            return self._get_height(node.right, key) + 1
        else:
            return 1


unbalanced_list = [20, 15, 10, 5, 8, 2]
balanced_list = [10, 5, 15, 2, 8, 20]

Binary_Search_Tree_unbalanced = Binary_Search_Tree(unbalanced_list)
Binary_Search_Tree_balanced = Binary_Search_Tree(balanced_list)

print("unbalanced", Binary_Search_Tree_unbalanced.is_avl())
print("balanced", Binary_Search_Tree_balanced.is_avl())

# Get the height of a random node from the list
random_node = random.choice(balanced_list)
height = Binary_Search_Tree_balanced.get_height(random_node)
print(f"Height of node {random_node}: {height}")
