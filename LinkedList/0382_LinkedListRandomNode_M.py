# https://leetcode.com/problems/linked-list-random-node/submissions/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1: 'select-and-keep', i.e., reservoir sampling with reservoir size = 1
import numpy as np
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        if self.head is None:
            return None

        # 'select-and-keep', i.e., reservoir sampling with reservoir size = 1
        res = self.head.val
        node = self.head.next
        i = 0
        while node is not None:
            i += 1
            rdn = np.random.randint(0, i+1)
            if rdn == 0:
                res =  node.val
            node = node.next

        return res
        
