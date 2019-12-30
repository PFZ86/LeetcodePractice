# https://leetcode.com/problems/combinations/

# Solution 1: dfs; condition on i is included or not; relatively slow.
class Solution(object):
    def combine_helper(self, n, k, i, path, result):
        if len(path) == k:
            result.append(path[:]) # result.append(path) is wrong
            return

        if i > n:
            return

        # i is included
        path.append(i)
        self.combine_helper(n, k, i + 1, path, result)
        del path[-1]

        # i is not included
        self.combine_helper(n, k, i + 1, path, result)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        path, result = [], []

        self.combine_helper(n, k, 1, path, result)

        return result

# Solution 2: dfs; 'start_idx' trick; faster than Solution 1
class Solution(object):
    def combine_helper(self, n, k, start_idx, path, result):
        if len(path) == k:
            result.append(path[:]) # result.append(path) is wrong
            return

        if start_idx > n:
            return

        for i in range(start_idx, n+1):
            path.append(i)
            self.combine_helper(n, k, i + 1, path, result)
            del path[-1]

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        path, result = [], []

        self.combine_helper(n, k, 1, path, result)

        return result
