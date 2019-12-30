# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: recursive, preorder
class Solution(object):
    def isSymmetric_helper(self, left, right):
        if left is None and right is None:
            return True
        if left is None and right is not None:
            return False
        if left is not None and right is None:
            return False
        if left.val != right.val:
            return False

        return self.isSymmetric_helper(left.left, right.right) and self.isSymmetric_helper(left.right, right.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.isSymmetric_helper(root.left, root.right)

# Solution 2: iterative, bfs
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        queue = [root.left, root.right]
        while len(queue) > 0:
            a = queue.pop(0)
            b = queue.pop(0)

            if a is None and b is None:
                continue
            if a is None and b is not None:
                return False
            if a is not None and b is None:
                return False
            if a.val != b.val:
                return False

            queue.append(a.left)
            queue.append(b.right)
            queue.append(a.right)
            queue.append(b.left)

        return True
