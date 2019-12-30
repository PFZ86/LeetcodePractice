# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# Solution 1: use two queues; swap them every time go deeper 1-level
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res, curr_node_q, next_node_q = [], [], []

        curr_node_q.append(root)
        while len(curr_node_q) > 0:
            res.append([])
            for node in curr_node_q:
                res[-1].append(node.val)
                for child in node.children:
                    next_node_q.append(child)
            curr_node_q, next_node_q = next_node_q[:], []

        return res
    
