# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: dp; top-down
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob_helper(node, canRob):
            if node is None:
                return 0

            profit_skip_node = rob_helper(node.left, True) + rob_helper(node.right, True)
            if canRob:
                profit_rob_node = node.val + rob_helper(node.left, False) + rob_helper(node.right, False)
                return max(profit_rob_node, profit_skip_node)
            else:
                return profit_skip_node

        return rob_helper(root, True)

# Solution 2: dp; top-down; memorization
'''
Need to differentiate between (node, canRob) and (node, cantRob) even for the same node.
'''
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob_helper(node, canRob):
            if node is None:
                return 0

            if canRob and node in mydict_can:
                return mydict_can[node]

            if not canRob and node in mydict_cant:
                return mydict_cant[node]

            profit_skip_node = rob_helper(node.left, True) + rob_helper(node.right, True)
            if canRob:
                profit_rob_node = node.val + rob_helper(node.left, False) + rob_helper(node.right, False)
                res = max(profit_rob_node, profit_skip_node)
            else:
                res = profit_skip_node

            if canRob:
                mydict_can[node] = res
            else:
                mydict_cant[node] = res

            return res

        mydict_can = {}
        mydict_cant = {}

        return rob_helper(root, True)
        
