'''
https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45468/3-Different-Solutions
'''
def preorder_iterative(root):
    stack = [root]

    while len(stack) > 0:
        node = stack[-1]
        del stack[-1]

        if node is None:
            continue

        stack.append(node.right)
        stack.append(node.left)

        doSomething(node.val)
        
