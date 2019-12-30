# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: bfs using two vectors
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        curr_level, next_level = [], []

        if root is None:
            return res

        curr_level.append(root)
        
        while len(curr_level):
            total, num = 0.0, 0.0
            for node in curr_level:
                num += 1
                total += node.val
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            res.append(total/num)
            curr_level, next_level = next_level[:], []

        return res
