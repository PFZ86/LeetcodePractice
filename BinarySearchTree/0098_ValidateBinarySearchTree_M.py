# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: the recursive solution
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(node, low_bound, upp_bound):
            if node is None:
                return True

            # node.val is out of bound
            if (low_bound is not None and node.val <= low_bound) or (upp_bound is not None and node.val >= upp_bound):
                return False

            return validate(node.left, low_bound, node.val) and validate(node.right, node.val, upp_bound)

        return validate(root, None, None)

# Solution 2: the iterative solution
'''
Iterative inorder traversal of binary tree
https://github.com/PFZ86/LeetcodePractice/blob/master/Tree/BinaryTreeIterativeInOrderTraversal.py
'''
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        visit = root
        stack = []

        prev_value = None
        while visit is not None or len(stack) > 0:
            while visit is not None:
                stack.append(visit)
                visit = visit.left

            node = stack[-1]
            del stack[-1]
            visit = node.right

            if prev_value is not None and node.val <= prev_value:
                return False
            prev_value = node.val

        return True
        
