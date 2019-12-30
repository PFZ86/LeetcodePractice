# https://leetcode.com/problems/bulls-and-cows/

# Solution 1: compute bull; compute bull+cow
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # compute bull
        bull = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
        # compute bull+cow
        from collections import Counter
        secret_counter = Counter(secret)
        guess_counter = Counter(guess)
        total = 0
        for g in guess_counter:
            if g in secret_counter:
                total += min(secret_counter[g], guess_counter[g])

        return '{}A{}B'.format(bull, total-bull)
