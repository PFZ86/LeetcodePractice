# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        curr = head

        carry = 0
        while l1 is not None or l2 is not None:
            v1 = 0 if l1 is None else l1.val
            v2 = 0 if l2 is None else l2.val
            tmp = carry + v1 + v2
            carry = tmp/10
            curr.next = ListNode(tmp%10)

            curr = curr.next
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        if carry:
            curr.next = ListNode(carry)

        return head.next
        
