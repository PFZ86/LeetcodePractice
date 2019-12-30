# https://leetcode.com/problems/k-diff-pairs-in-an-array/

# Solution 1
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = nums[:]
        nums = sorted(nums)

        firstNumList = []
        mydict = {}

        for num in nums:
            if num - k in mydict and num not in firstNumList:
                firstNumList.append(num)

            mydict[num] = 1

        return len(firstNumList)
        
