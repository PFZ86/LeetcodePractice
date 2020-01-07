# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: the recursive solution
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder_traversal(node):
            if node is None:
                return
            res.append(node.val)
            preorder_traversal(node.left)
            preorder_traversal(node.right)

        res = []
        preorder_traversal(root)

        return res

# Solution 2: the iterative solution
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack[-1]
            del stack[-1]
            if node is None:
                continue

            stack.append(node.right)
            stack.append(node.left)

            res.append(node.val)

        return res
        
