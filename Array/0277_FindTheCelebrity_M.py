# https://www.cnblogs.com/grandyang/p/5310649.html

# Solution 1
class Solution:
    def findCelebrity(self, n):
        maybe = [True] * n
        for i in range(n):
            if not maybe[i]:
                continue
            for j in range(n):
                if j == i:
                    continue
                if Celebrity.knows(i, j) or (not Celebrity.knows(j, i)):
                    maybe[i] = False
                if Celebrity.knows(j, i) or (not Celebrity.knows(i, j)):
                    maybe[j] = False
                if not maybe[i]:
                    break
            # if i is not rejected after looping over all other people,
            # then i is the celebrity.
            if maybe[i]:
                return i
        return -1

# Solution 2
class Solution:
    def findCelebrity(self, n):
        res = 0
        # find the possible celebrity.
        for i in range(n):
            if Celebrity.knows(res, i):
                res = i
        # verify he/she is the celebrity.
        for i in range(n):
            if i == res:
                continue
            if Celebrity.knows(res, i) or (not Celebrity.knows(i, res)):
                return -1
        return res
