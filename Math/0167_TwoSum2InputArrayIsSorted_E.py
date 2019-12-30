# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Solution 1: the two-pointer method
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i, j = 0, len(numbers) - 1
        while i < j:
            sumij = numbers[i] + numbers[j]
            if sumij == target:
                return [i+1, j+1]

            if sumij < target:
                i += 1
                while i < j and numbers[i] == numbers[i-1]:
                    i += 1
            else:
                j -= 1
                while j > i and numbers[j] == numbers[j+1]:
                    j -= 1
