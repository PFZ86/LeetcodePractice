# https://leetcode.com/problems/subsets/submissions/

# Solution 1: dfs; condition on nums[i] is included or not
class Solution(object):
    def subsets_helper(self, nums, idx, path, result):
        if idx == len(nums):
            result.append(path[:]) # ! result.append(path) is wrong

            return

        # nums[idx] is included
        path.append(nums[idx])
        self.subsets_helper(nums, idx + 1, path, result)
        del path[-1]

        # nums[idx] is not included
        self.subsets_helper(nums, idx + 1, path, result)

        return

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        path, result = [], []

        self.subsets_helper(nums, 0, path, result)

        return result

# Solution 2: dfs; 'start_idx'; much slower than Solution 1
class Solution(object):
    def subsets_helper(self, nums, start_idx, path, result):
        if start_idx == len(nums) and path not in result:
            result.append(path[:]) # ! result.append(path) is wrong

            return

        for i in range(start_idx, len(nums)):
            path.append(nums[i])
            self.subsets_helper(nums, i + 1, path, result)
            del path[-1]

            self.subsets_helper(nums, i + 1, path, result)

        return

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        path, result = [], []

        self.subsets_helper(nums, 0, path, result)

        return result
