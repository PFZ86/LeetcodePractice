# https://leetcode.com/problems/3sum/

# Solution 1: sort the array first; then use the two-pointer method
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        solutions = []

        i = 0
        while i <= (len(nums) - 3):
            j, k = i + 1, len(nums) - 1

            while j < k:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    solutions.append([nums[i], nums[j], nums[k]])

                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif (nums[i] + nums[j] + nums[k]) < 0:
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
