# https://leetcode.com/problems/permutations/

# Solution 1: dfs.
# The 'startIndex' method is not good for this problem, since every element needs to be in the permutation.
class Solution(object):
    def permute_helper(self, nums, path, result):
        if len(path) == len(nums):
            result.append(path[:]) # result.append(path) is wrong
        else:
            for num in nums:
                if num not in path:
                    path.append(num)
                    self.permute_helper(nums, path, result)
                    del path[-1] # remember to restore the path

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path, result = [], []
        self.permute_helper(nums, path, result)

        return result

# https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python
# Solution 2: recursive
# Take any number as the first number and append any permutation of the other numbers.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        return [[num] + p
                for idx, num in enumerate(nums)
                for p in self.permute(nums[:idx] + nums[(idx+1):])]

# https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python
# Solution 3: recursive
# Insert the first number anywhere in any permutation of the remaining numbers.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        return [p[:i] + [nums[0]] + p[i:]
                for p in self.permute(nums[1:])
                for i in range(len(nums))]
                
