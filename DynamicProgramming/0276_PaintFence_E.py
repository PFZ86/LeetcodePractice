# https://www.lintcode.com/problem/paint-fence/description

# Solution 1: dp; bottom-up
'''
If i has different color than (i-1):
    then it is straightforward to get (k-1)*dp[i-1]
If i has same color as (i-1):
    then i and (i-1) become the same, the problem reduces to compare (i-1) with (i-2),
    so we can get (k-1)*dp[i-2]
'''
class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[0] = k
            elif i == 1:
                dp[1] = k**2
            else:
                dp[i] = (k-1)*dp[i-1] + (k-1)*dp[i-2]

        return dp[-1]
