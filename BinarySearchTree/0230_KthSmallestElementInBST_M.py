# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: recursive inorder traversal
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        nums = []
        inorder(root)

        return nums[k-1]

# Solution 2: iterative inorder traversal
'''
https://github.com/PFZ86/LeetcodePractice/blob/master/Tree/BinaryTreeIterativeInOrderTraversal.py
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        visit = root
        stack = []

        while visit is not None or len(stack) > 0:
            while visit is not None:
                stack.append(visit)
                visit = visit.left

            node = stack[-1]
            del stack[-1]
            visit = node.right

            k -= 1
            if k == 0:
                return node.val
            
