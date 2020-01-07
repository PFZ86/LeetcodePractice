# https://leetcode.com/problems/minimum-distance-between-bst-nodes/discuss/?currentPage=1&orderBy=most_votes&query=

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: the recursive solution
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            global mindist, prev_value
            if prev_value is not None:
                mindist = min(mindist, node.val - prev_value)
            prev_value = node.val
            inorder(node.right)

            return

        global mindist
        mindist = float('inf')

        global prev_value
        prev_value = None

        inorder(root)

        return mindist
        
# Solution 2: the iterative solution
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        mindist = float('inf')
        prev_value = None

        visit = root
        stack = []

        while visit is not None or len(stack) > 0:
            while visit is not None:
                stack.append(visit)
                visit = visit.left

            node = stack[-1]
            del stack[-1]
            visit = node.right

            if prev_value is not None:
                mindist = min(mindist, node.val -  prev_value)

            prev_value = node.val

        return mindist
