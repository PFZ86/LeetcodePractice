# https://leetcode.com/problems/elimination-game/

# Solution 1: recursive; top-down (memorization)
# (1) first: notice that f(2k+1) = f(2k)
# (2) second: by 2, 4,  6, 8, ..., 2k-2, 2k
#                k, k-1, .........,   2,  1
# we have f(2k) + 2f(k) = 2k+2. Therefore f(2k) = 2k + 2 - 2*f(k)

class Solution(object):
    def lastRemaining_helper(self, i, result):
        if i in result:
            return result[i]

        if i%2 == 1:
            tmp = self.lastRemaining_helper(i-1, result)
        else:
            tmp = i + 2 - 2*self.lastRemaining_helper(i/2, result)

        result[i] = tmp
        return tmp

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = {}
        result[1] = 1

        return self.lastRemaining_helper(n, result)
    
