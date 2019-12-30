# https://leetcode.com/problems/rotate-function/

# Solution 1: use deque.rotate
from collections import deque
import numpy as np

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0

        D = deque(A)
        fixed = [x for x in range(len(A))]
        result = None

        for i in range(len(A)):
            tmp = np.sum(np.multiply(fixed, D))
            if result is None or result < tmp:
                result = tmp
            D.rotate(1)

        return result

# Solution 2: find the relationship between F(i) and F(i+1)
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total, curr, length = 0, 0, len(A)
        for idx, num in enumerate(A):
            total += num
            curr += idx*num

        result = curr
        for i in range(1, length):
            curr += (total - length*A[length - i])
            result = max(result, curr)

        return result
