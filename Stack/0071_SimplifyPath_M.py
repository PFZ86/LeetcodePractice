# https://leetcode.com/problems/simplify-path/

# Solution 1
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        """
        '/home/'.split('/')
        ['', 'home', '']

        '/../'.split('/')
        ['', '..', '']

        '/a/./b/../../c/'.split('/')
        ['', 'a', '.', 'b', '..', '..', 'c', '']
        """
        path_split = path.split('/')
        mystack = []
        for s in path_split:
            if s in ['', '.']:
                continue
            elif s == '..':
                if len(mystack) > 0:
                    del mystack[-1]
            else:
                mystack.append(s)

        return '/' + '/'.join([x for x in mystack if x != '..'])
