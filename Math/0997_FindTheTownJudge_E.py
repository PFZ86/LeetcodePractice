# https://leetcode.com/problems/find-the-town-judge/

# Solution 1
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        judge_score = [0 for _ in range(N)]
        for a, b in trust:
            judge_score[a-1] -= 1
            judge_score[b-1] += 1

        for i in range(N):
            if judge_score[i] == (N-1):
                return i+1

        return -1
        
