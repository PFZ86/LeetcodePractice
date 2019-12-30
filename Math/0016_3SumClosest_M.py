# https://leetcode.com/problems/3sum-closest/

# Solution 1: sort the array first; then use the two-pointer method
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)

        result, min_dist = None, None

        i = 0
        while i <= (len(nums)-3):
            j, k = i+1, len(nums)-1
            while j < k:
                this_sum = nums[i] + nums[j] + nums[k]
                this_diff = this_sum - target

                if this_diff == 0:
                    return target

                if min_dist is None or abs(this_diff) < min_dist:
                    result = this_sum
                    min_dist = abs(this_diff)

                if this_diff < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
            i += 1
            while i <= (len(nums)-3) and nums[i] == nums[i-1]:
                i += 1

        return result
