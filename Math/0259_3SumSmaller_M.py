# https://www.lintcode.com/problem/3sum-smaller/description

# Solution 1: sort the array first; then use the two-pointer method
class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        nums = sorted(nums)
        result = 0

        i = 0
        while i <= (len(nums)-3):
            j, k = i+1, len(nums)-1
            while j < k:
                this_sum = nums[i] + nums[j] + nums[k]
                if this_sum >= target:
                    k -= 1
                else:
                    # (i,j,j+1), (i,j,j+2) ... (i,j,k) all satisfy the requirement
                    result += (k-j)
                    j += 1
            i += 1

        return result
