# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: the recursive solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder_traversal(node):
            if node is None:
                return
            inorder_traversal(node.left)
            res.append(node.val)
            inorder_traversal(node.right)

        res = []
        inorder_traversal(root)

        return res

# Solution 2: the iterative solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        visit = root
        stack = []
        while visit is not None or len(stack) > 0:
            while visit is not None:
                stack.append(visit)
                visit = visit.left

            node = stack[-1]
            del stack[-1]
            visit = node.right

            res.append(node.val)

        return res
        
