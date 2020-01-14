# https://leetcode.com/problems/longest-turbulent-subarray/

# Solution 1
'''
Compare the sign of consecutive pairwise difference. There are 3 possible actions:
(1) Extend the current turbulent subarray by including A[i]
(2) Restart a turbulent subarray with A[i]
(3) Restart a turbulent subarray with A[i-1], A[i]
'''
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 1:
            return len(A)

        prev_diff = A[1] - A[0]
        max_len = 1 if prev_diff == 0 else 2 # [9, 9]

        res = max_len
        for i in range(2, len(A)):
            curr_diff = A[i] - A[i-1]
            if (curr_diff*prev_diff) < 0:
                max_len += 1 # extend the current turbulent subarray by including A[i]
            elif curr_diff == 0: # [9, 9, 9]
                max_len = 1 # restart a turbulent subarray with A[i]
            else:
                max_len = 2 # restart a turbulent subarray with A[i-1], A[i]

            prev_diff = curr_diff
            res = max(res, max_len)

        return res
        
