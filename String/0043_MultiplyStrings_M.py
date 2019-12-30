# https://leetcode.com/problems/multiply-strings/

# Solution 1: use carry
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        n1, n2 = len(num1), len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        # len(num1*num2) is at most len(num1) + len(num2)
        result = [0] * (n1 + n2)

        for i in range(n1):
            for j in range(n2):
                result[i+j] += int(num1[i])*int(num2[j])

        carry = 0
        for k in range(n1+n2):
            tmp = carry + result[k]
            result[k], carry = tmp%10, tmp/10

        # remove the last 0 so the final result does not have a leading 0s.
        # otherwise, "2"*"3" gives "06".
        if result[-1] == 0:
            del result[-1]

        return ''.join([str(x) for x in reversed(result)])
        
