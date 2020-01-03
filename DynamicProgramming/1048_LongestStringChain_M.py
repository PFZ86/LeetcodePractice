# https://leetcode.com/problems/longest-string-chain/

# Solution 1: dp; top-down, memorization
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def find_max_chain_len(word):
            if word not in words:
                return 0

            if word not in word_to_max_chain_len:
                tmp = 0
                for i in range(len(word)):
                    new_word = word[:i] + word[(i+1):]
                    tmp = max(tmp, find_max_chain_len(new_word))
                word_to_max_chain_len[word] = tmp + 1

            return word_to_max_chain_len[word]

        word_to_max_chain_len = {}
        max_chain_len = 0
        for word in words:
            if word not in word_to_max_chain_len:
                word_to_max_chain_len[word] = find_max_chain_len(word)
            max_chain_len = max(max_chain_len, word_to_max_chain_len[word])

        return max_chain_len
            
