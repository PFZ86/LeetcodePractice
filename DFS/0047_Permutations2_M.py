# https://leetcode.com/problems/permutations-ii/

# Solution 1: dfs; sort the array first; use a 'used' vector
# https://leetcode.com/problems/permutations-ii/discuss/18596/A-simple-C%2B%2B-solution-in-only-20-lines
class Solution(object):
    def permuteUnique_helper(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path[:])
        else:
            for idx, num in enumerate(nums):
                if used[idx] or (idx > 0 and nums[idx-1] == nums[idx] and not used[idx-1]):
                    continue

                used[idx] = True
                path.append(num)
                self.permuteUnique_helper(nums, used, path, result)
                used[idx] = False
                del path[-1]

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort the array
        nums = sorted(nums)

        path, result = [], []
        used = [False for _ in range(len(nums))]

        self.permuteUnique_helper(nums, used, path, result)

        return result
        
