# https://leetcode.com/problems/unique-morse-code-words/

# Solution 1
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import string

        letter_list = list(string.ascii_lowercase)
        code_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        letter_to_code = dict(zip(letter_list, code_list))

        code_set = set()
        for word in words:
            code = ''
            for letter in word:
                code += letter_to_code[letter]
            code_set.add(code)

        return len(code_set)

# Solution 2
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        code_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        code_set = set()
        for word in words:
            code = ''
            for letter in word:
                code += code_list[ord(letter) - ord('a')]
            code_set.add(code)

        return len(code_set)
        
