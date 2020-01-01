# https://www.lintcode.com/problem/sentence-similarity/description

# Solution 1:
class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False

        mydict = {}
        for [x, y] in pairs:
            if x not in mydict:
                mydict[x] = []
            if y not in mydict[x]:
                mydict[x].append(y)

            if y not in mydict:
                mydict[y] = []
            if x not in mydict[y]:
                mydict[y].append(x)

        for w1, w2 in zip(words1, words2):
            if (w1 != w2) and (w1 not in mydict or w2 not in mydict[w1]):
                return False

        return True
        
