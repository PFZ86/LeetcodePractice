# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: binary search-like split
class Solution(object):
    def sortedArrayToBST_helper(self, nums, start, end):
        if start > end:
            return None

        mid = start + (end - start)/2

        node = ListNode(nums[mid])
        node.left = self.sortedArrayToBST_helper(nums, start, mid - 1)
        node.right = self.sortedArrayToBST_helper(nums, mid + 1, end)

        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        return self.sortedArrayToBST_helper(nums, 0, len(nums) - 1)
        
