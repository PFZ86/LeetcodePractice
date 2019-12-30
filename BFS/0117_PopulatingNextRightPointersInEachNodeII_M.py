# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

### Solution 1: breath-first traverse a binary tree
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return

        curr_level = []
        next_level = []

        curr_level.append(root)

        while len(curr_level):
            for idx in range(len(curr_level)):
                node = curr_level[idx]
                if idx < len(curr_level) - 1:
                    node.next = curr_level[idx+1]
                else:
                    node.next = None

                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            curr_level = next_level[:]
            next_level = []

        return root
