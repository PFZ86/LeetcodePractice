# https://leetcode.com/problems/super-ugly-number/

# Solution 1: the Sieve method
'''
indexes of 2, 7, 13, 19      super_ugly_numbers
           0, 0,  0,  0      1
           1, 0,  0,  0      1, 2
           2, 0,  0,  0      1, 2, 4
           2, 1,  0 , 0      1, 2, 4, 7
           3, 1,  0 , 0      1, 2, 4, 7, 8
           3, 1,  1,  0      1, 2, 4, 7, 8, 13
           4, 2,  1,  0      1, 2, 4, 7, 8, 13, 14
           5, 2,  1,  0      1, 2, 4, 7, 8, 13, 14, 16
           5, 2,  1,  1      1, 2, 4, 7, 8, 13, 14, 16, 19
           6, 2,  2,  1      1, 2, 4, 7, 8, 13, 14, 16, 19, 26
           7, 3,  2,  1      1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28
           8, 3,  2,  1      1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32
'''

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        num_primes = len(primes)
        prime_idx = [0 for _ in range(num_primes)]

        super_ugly_nums = [1]
        while len(super_ugly_nums) < n:
            candidates = [super_ugly_nums[prime_idx[i]] * primes[i] for i in range(num_primes)]
            next_super_ugly_num = min(candidates)
            for i in range(num_primes):
                if next_super_ugly_num == candidates[i]:
                    prime_idx[i] += 1
            super_ugly_nums.append(next_super_ugly_num)

        return super_ugly_nums[-1]
        
