'''
https://leetcode.com/problems/binary-search-tree-iterator/discuss/52647/Nice-Comparison-(and-short-Solution)
'''
def inorder_iterative(root):
    visit = root
    stack = []

    while visit is not None or len(stack):
        while visit is not None:
            stack.append(visit)
            visit = visit.left

        node = stack[-1]
        del stack[-1]
        visit = node.right

        doSomething(node.val)
        
