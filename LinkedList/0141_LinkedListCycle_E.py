# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1: 'slow-fast' pointer.
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return False

        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            if slow.val == fast.val:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
        
