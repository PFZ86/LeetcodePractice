# https://leetcode.com/problems/4sum/

# Solution 1: sort the array first and then threeSum
class Solution(object):
    def threeSum(self, nums, start_idx, target):
        solutions = []

        i = start_idx + 1
        while i <= (len(nums) - 3):
            j, k = i + 1, len(nums) - 1

            while j < k:
                if (nums[i] + nums[j] + nums[k]) == target:
                    solutions.append([nums[i], nums[j], nums[k]])

                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif (nums[i] + nums[j] + nums[k]) < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1

            i += 1
            while i <= (len(nums) - 3) and nums[i] == nums[i-1]:
                i += 1

        return solutions

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        solutions = []

        start = 0
        while start <= (len(nums) - 4):
            sols = self.threeSum(nums, start, target - nums[start])
            for sol in sols:
                solutions.append([nums[start]] + sol)

            start += 1
            while start <= (len(nums) - 4) and nums[start] == nums[start-1]:
                start += 1

        return solutions
