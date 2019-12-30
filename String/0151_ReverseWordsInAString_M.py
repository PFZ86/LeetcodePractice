# https://leetcode.com/problems/reverse-words-in-a-string/

# Solution 1: first reverse each word in the string; then reverse the whole string
class Solution(object):
    def reverseOneWord(self, word):
        letter_list = list(word)
        i, j = 0, len(letter_list) - 1
        while i < j:
            letter_list[i], letter_list[j] = letter_list[j], letter_list[i]
            i += 1
            j -= 1

        return ''.join(letter_list)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.lstrip(' ').rstrip(' ').split()
        for k in range(len(word_list)):
            word_list[k] = self.reverseOneWord(word_list[k])

        return self.reverseOneWord(' '.join(word_list))
        
