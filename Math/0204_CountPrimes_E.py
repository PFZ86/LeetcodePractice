# https://leetcode.com/problems/count-primes/

# Solution 1: the naive method, time complexity O(n^{1.5})
class Solution(object):
    def isPrime(self, num):
        if num <= 1:
            return False

        i = 2
        # Use i*i <= num as the ending condition;
        # do not use the expensive function sqrt(num)
        while i*i <= num:
            if num % i == 0:
                return False
            i += 1

        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1, n):
            if self.isPrime(i):
                count += 1

        return count

# Solution 2: the Sieve method; time complexity O(nloglogn), space complexity O(n)
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True] * n

        i = 2
        # the ending condition is i*i <= n instead of i <= sqrt(n)
        for i in range(2, n):
            if i*i > n:
                break
            if isPrime[i]:
                # we can start from i*i because multiples of i that
                # are less than i*i are already marked as non-prime
                j = i*i
                while j < n:
                    isPrime[j] = False
                    j += i

        return sum(isPrime[2:])
