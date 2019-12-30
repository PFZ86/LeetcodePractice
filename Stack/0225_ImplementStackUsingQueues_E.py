# https://leetcode.com/problems/implement-stack-using-queues/

# Solution 1: Use two queues.
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.q1):
            res = self.q1[0]
            del self.q1[0]
            self.q2.append(res)

        while len(self.q2) > 1:
            self.q1.append(self.q2[0])
            del self.q2[0]

        self.q2 = []

        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while len(self.q1):
            res = self.q1[0]
            del self.q1[0]
            self.q2.append(res)

        while len(self.q2) :
            self.q1.append(self.q2[0])
            del self.q2[0]

        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """

        return len(self.q1) == 0

# Solution 2: https://leetcode.com/problems/implement-stack-using-queues/discuss/62516/Concise-1-Queue-Java-C%2B%2B-Python
# Use one queue: 'push to front" by pushing to back and then rotating the queue until
# the new element is at the front (i.e., size-1 times move the front element to the back).
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            tmp = self.q[0]
            del self.q[0]
            self.q.append(tmp)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        res = self.q[0]
        del self.q[0]

        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """

        return len(self.q) == 0
        
