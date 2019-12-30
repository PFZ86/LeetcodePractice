# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: inorder traserval of BST; merge two sorted arrays.
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        # in-order traversal
        def inorder(root, values):
            if root:
                inorder(root.left, values)
                values.append(root.val)
                inorder(root.right, values)

        values1 = []
        inorder(root1, values1)

        values2 = []
        inorder(root2, values2)

        # merge two sorted arrays
        res = []
        idx1 = 0
        idx2 = 0
        while idx1 < len(values1) and idx2 < len(values2):
            if values1[idx1] <= values2[idx2]:
                res.append(values1[idx1])
                idx1 += 1
            else:
                res.append(values2[idx2])
                idx2 += 1

        while idx1 < len(values1):
            res.append(values1[idx1])
            idx1 += 1

        while idx2 < len(values2):
            res.append(values2[idx2])
            idx2 += 1

        return res
        
