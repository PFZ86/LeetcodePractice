# https://www.lintcode.com/problem/paint-house-ii/description

# Solution 1: dp; bottom-up
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        if len(costs) == 0:
            return 0

        n, k = len(costs), len(costs[0])
        dp = [[float('inf')] * k for _ in range(n)]

        for i in range(n):
            for j in range(k):
                if i == 0:
                    dp[0][j] = costs[0][j]
                else:
                    for other in range(k):
                        if other != j:
                            dp[i][j] = min(dp[i][j], dp[i-1][other] + costs[i][j])

        res = float('inf')
        for j in range(k):
            res = min(res, dp[-1][j])

        return res
        
