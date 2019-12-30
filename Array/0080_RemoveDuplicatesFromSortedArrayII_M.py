# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Solution 1: this solution can be easily generalized to "at most K duplicates"
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C%2B%2B-Java-Python-Ruby
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        K = 2
        for j in range(len(nums)):
            if i < K or nums[j] > nums[i-K]:
                nums[i] = nums[j]
                i += 1
        return i
