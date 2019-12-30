# https://leetcode.com/problems/super-ugly-number/

# Solution 1: the Sieve method
# indexes of 2, 7, 13, 19      super_ugly_numbers
#            0, 0,  0,  0      1
#            1, 0,  0,  0      1, 2
#            2, 0,  0,  0      1, 2, 4
#            2, 1,  0 , 0      1, 2, 4, 7
#            3, 1,  0 , 0      1, 2, 4, 7, 8
#            3, 1,  1,  0      1, 2, 4, 7, 8, 13
#            4, 2,  1,  0      1, 2, 4, 7, 8, 13, 14
#            5, 2,  1,  0      1, 2, 4, 7, 8, 13, 14, 16
#            5, 2,  1,  1      1, 2, 4, 7, 8, 13, 14, 16, 19
#            6, 2,  2,  1      1, 2, 4, 7, 8, 13, 14, 16, 19, 26
#            7, 3,  2,  1      1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28
#            8, 3,  2,  1      1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        super_ugly_numbers = [1]
        prime_indexes = [0] * len(primes)

        while len(super_ugly_numbers) < n:
            candidates = []

            for i in range(len(primes)):
                candidates.append(super_ugly_numbers[prime_indexes[i]] * primes[i])
            this_super_ugly_number = min(candidates)

            for i in range(len(primes)):
                if candidates[i] == this_super_ugly_number:
                    prime_indexes[i] += 1

            super_ugly_numbers.append(this_super_ugly_number)

        return super_ugly_numbers[n-1]
        
