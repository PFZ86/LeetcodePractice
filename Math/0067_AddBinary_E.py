# https://leetcode.com/problems/add-binary/

# Solution 1:
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        n = max(len(a), len(b))

        result = []
        carry = 0
        for i in range(n):
            digit_a = 0 if i >= len(a) else int(a[i])
            digit_b = 0 if i >= len(b) else int(b[i])
            tmp = (digit_a + digit_b + carry)
            result.append(str(tmp%2))
            carry = tmp / 2

        # check carry after the for-loop
        if carry:
            result.append(str(carry))

        return ''.join(result)[::-1]
        
