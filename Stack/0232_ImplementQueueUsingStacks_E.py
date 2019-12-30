# https://leetcode.com/problems/implement-queue-using-stacks/

# Solution 1: use two stacks.
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.s2) == 0:
            while len(self.s1):
                self.s2.append(self.s1[-1])
                del self.s1[-1]

        if len(self.s2) > 0:
            res = self.s2[-1]
            del self.s2[-1]
            return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.s2) == 0:
            while len(self.s1):
                self.s2.append(self.s1[-1])
                del self.s1[-1]

        if len(self.s2) > 0:
            return self.s2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0
        
