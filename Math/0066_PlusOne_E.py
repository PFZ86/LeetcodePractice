# https://leetcode.com/problems/plus-one/

# Solution 1: use the 'carry' variable
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        carry = 1
        for digit in reversed(digits):
            result.insert(0, (digit + carry)%10)
            carry = (digit + carry)/10

        # check the last carry
        if carry != 0:
            result.insert(0, carry)

        return result
        
