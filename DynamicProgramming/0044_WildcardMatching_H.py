# https://leetcode.com/problems/wildcard-matching/

# Solution 1: naive recursive
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == '':
            return p.count('*') == len(p)
        if p == '':
            return s == ''
        if p[0] == '?' or p[0] == s[0]:
            return self.isMatch(s[1:], p[1:])
        if p[0] == '*':
            # p[0] is used or p[0] is not used
            return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])

        return False

# Solution 2: dp; top-down; memorization
'''
Two optimizations over Solution 1:
    Change passing str to passing start_index to save memory in recursive calls.
    Avoid duplicated computation by memorization.
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def isMatch_helper(s_start, p_start):
            if (s_start, p_start) in mydict:
                return mydict[(s_start, p_start)]

            res = False
            if s_start == len(s):
                res = p[p_start:].count('*') == (len(p) - p_start)
            elif p_start == len(p):
                res = s_start == len(s)
            elif p[p_start] == '?' or p[p_start] == s[s_start]:
                res = isMatch_helper(s_start+1, p_start+1)
            elif p[p_start] == '*':
                # p[p_start] is used or p[p_start] is not used.
                res = isMatch_helper(s_start+1, p_start) or isMatch_helper(s_start, p_start+1)

            mydict[(s_start, p_start)] = res
            return res

        mydict = {}

        return isMatch_helper(0, 0)

# Solution 3: dp; bottom-up
'''
One nice trick is to use the last row and the last column of the dp matrix to handle corner cases.
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]

        # use the last row and last column to handle corner cases:
        # corner case: '' matches ''
        dp[-1][-1] = True
        # corner case: '' matches sequence of '*'
        for j in range(len(p)):
            if p[j] != '*':
                break
            dp[-1][j] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '?' or p[j] == s[i]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[len(s)-1][len(p)-1]

# Solution 4: greedy, backtracking.
'''
https://www.iteye.com/blog/shmilyaw-hotmail-com-2154716
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        si, pi = 0, 0
        last_si, last_pi = -1, -1

        while si < len(s):
            if pi < len(p) and (p[pi] == '?' or p[pi] == s[si]):
                pi += 1
                si += 1
            elif pi < len(p) and p[pi] == '*':
                last_si = si
                last_pi = pi
                pi += 1
            elif last_pi >= 0:
                si = last_si + 1
                pi = last_pi + 1
                last_si += 1
            else:
                return False

        return p[pi:].count('*') == (len(p) - pi)
        
