# https://leetcode.com/problems/maximum-product-of-three-numbers/

# Solution 1: O(n) time, O(1) space
# The largest product is either largest1*largest2*largest3 or largest1*smallest1*smallest2
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort the first 3 numbers
        tmp = sorted(nums[0:3])
        large1, large2, large3 = tmp[2], tmp[1], tmp[0]
        small1, small2 = tmp[0], tmp[1]

        # start from the 4th number
        for num in nums[3:]:
            # keep track of the largest 3 numbers
            if num >= large1:
                large1, large2, large3 = num, large1, large2
            elif num >= large2:
                large2, large3 = num, large2
            elif num >= large3:
                large3 = num

            # keep track of the smallest 2 numbers.
            if num <= small1:
                small1, small2 = num, small1
            elif num <= small2:
                small2 = num

        return max(large1*large2*large3, small1*small2*large1)
        
