# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: inorder traversal of a BST gives the non-decreasing sequeuece.
class Solution(object):
    def __init__(self):
        self.prev_val = None
        self.curr_freq = 0
        self.max_freq = 0
        self.res = []

    def findMode_helper(self, node):
        if node is None:
            return

        # left child
        self.findMode_helper(node.left)

        # current node
        if node.val == self.prev_val:
            self.curr_freq += 1
        else:
            self.curr_freq = 1
        self.prev_val = node.val

        if self.curr_freq == self.max_freq:
            self.res.append(node.val)
        elif self.curr_freq > self.max_freq:
            self.res = [node.val]
            self.max_freq = self.curr_freq

        # right child
        self.findMode_helper(node.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.findMode_helper(root)

        return self.res
        
