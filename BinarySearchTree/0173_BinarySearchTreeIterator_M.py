# https://leetcode.com/problems/binary-search-tree-iterator/

# Solution 1:
'''
iterative inorder traversal of BST
https://leetcode.com/problems/binary-search-tree-iterator/discuss/52647/Nice-Comparison-(and-short-Solution)
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.visit = root
        self.stack = []


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        while self.visit is not None:
            self.stack.append(self.visit)
            self.visit = self.visit.left

        node = self.stack[-1]
        del self.stack[-1]
        self.visit = node.right

        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.visit is not None or len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
