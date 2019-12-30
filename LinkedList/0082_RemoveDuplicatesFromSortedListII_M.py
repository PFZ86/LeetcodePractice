# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1: the recursive method
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        if head.val == head.next.val:
            tmp = head
            while tmp is not None and tmp.val == head.val:
                tmp = tmp.next
            return self.deleteDuplicates(tmp)
        else:
            tmp = self.deleteDuplicates(head.next)
            head.next = tmp
            return head
