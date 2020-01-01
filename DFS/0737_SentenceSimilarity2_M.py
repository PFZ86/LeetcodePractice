# https://www.lintcode.com/problem/sentence-similarity-ii/description

# Solution 1: dfs
class Solution:
    """
    @param words1:
    @param words2:
    @param pairs:
    @return: Whether sentences are similary or not?
    """
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        def find(i, target):
            if i == target:
                return True
            if i not in mydict:
                return False
            if i not in visited:
                visited.add(i)
                for j in mydict[i]:
                    if find(j, target):
                        return True
            return False

        if len(words1) != len(words2):
            return False

        mydict = {}
        for [x, y] in pairs:
            if x not in mydict:
                mydict[x] = set()
            mydict[x].add(y)

            if y not in mydict:
                mydict[y] = set()
            mydict[y].add(x)

        for w1, w2 in zip(words1, words2):
            visited = set()
            if (w1 != w2) and not find(w1, w2):
                return False

        return True
        
