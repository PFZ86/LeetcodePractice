# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: recursive
class Solution(object):
    def sumOfLeftLeaves_helper(self, node, isLeft):
        if node is None:
            return 0

        if isLeft and node.left is None and node.right is None:
            return node.val

        return self.sumOfLeftLeaves_helper(node.left, True) + self.sumOfLeftLeaves_helper(node.right, False)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return self.sumOfLeftLeaves_helper(root.left, True) + self.sumOfLeftLeaves_helper(root.right, False)

# Solution 2: iterative (breath-first)
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        res, node_q = 0, [root]
        while len(node_q) > 0:
            node = node_q[0]
            del node_q[0]

            if node.left is not None:
                if node.left.left is None and node.left.right is None:
                    # node.left is a left leaf
                    res += node.left.val
                else:
                    node_q.append(node.left)

            if node.right is not None:
                node_q.append(node.right)

        return res
    
