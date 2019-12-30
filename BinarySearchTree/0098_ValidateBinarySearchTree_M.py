# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: recursive
class Solution(object):
    def isValidBST_helper(self, node, low_val, upp_val):
        if node is None:
            return True

        # node.val is out of valid range
        if (low_val is not None and node.val <= low_val) or (upp_val is not None and node.val >= upp_val):
            return False

        # valid range for left child
        left_valid = self.isValidBST_helper(node.left, low_val, node.val)
        # valid range for right chold
        right_valid = self.isValidBST_helper(node.right, node.val, upp_val)

        return left_valid and right_valid

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.isValidBST_helper(root, None, None)
