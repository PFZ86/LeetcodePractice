# https://leetcode.com/problems/powerful-integers/

# Solution 1
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        powers_x = [1]
        if x > 1:
            num = x
            while num < bound:
                powers_x.append(num)
                num *= x

        powers_y = [1]
        if y > 1:
            num = y
            while num < bound:
                powers_y.append(num)
                num *= y

        res = []
        for a in powers_x:
            for b in powers_y:
                tmp = a+b
                if tmp <= bound and tmp not in res:
                    res.append(tmp)

        return res
        
