# https://leetcode.com/problems/min-stack/

# Solution 1: use two lists
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._l1 = []
        self._l2 = []

        return

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._l1.append(x)
        if len(self._l2) == 0 or self._l2[-1] > x:
            self._l2.append(x)
        else:
            self._l2.append(self._l2[-1])

        return

    def pop(self):
        """
        :rtype: None
        """
        if len(self._l1):
            del self._l1[-1]
            del self._l2[-1]

        return

    def top(self):
        """
        :rtype: int
        """
        if len(self._l1):
            return self._l1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self._l2):
            return self._l2[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
