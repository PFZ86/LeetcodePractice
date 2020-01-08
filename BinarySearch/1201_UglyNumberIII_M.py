# https://leetcode.com/problems/ugly-number-iii/

# Solution 1:
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        na, nb, nc = a, b, c

        ugly_nums = []
        while len(ugly_nums) < n:
            next_ugly_num = min([na, nb, nc])
            if next_ugly_num == na:
                na += a
            if next_ugly_num == nb:
                nb += b
            if next_ugly_num == nc:
                nc += c

            ugly_nums.append(next_ugly_num)

        return ugly_nums[-1]

# Solution 2: binary search
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def gcd(n1, n2):
            if n2 == 0:
                return n1
            return gcd(n2, n1%n2)

        def lcm(n1, n2):
            return n1*n2 // gcd(n1, n2)

        def count_ugly_number(n):
            return n//a + n//b + n//c - n//lcm_ab - n//lcm_ac - n//lcm_bc + n//lcm_abc

        lcm_ab = lcm(a, b)
        lcm_ac = lcm(a, c)
        lcm_bc = lcm(b, c)
        lcm_abc = lcm(lcm_ab, c)

        low, high = 1, n*min([a, b, c])
        while low < high:
            mid = low + (high - low) // 2
            count = count_ugly_number(mid)
            if count < n:
                low = mid + 1
            else:
                high = mid

        return low
        
