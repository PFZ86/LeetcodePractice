### define TreeNode class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

### construct A complete binary tree from a list of numbers
class CompleteBinaryTreeConstructor(object):
    def construct(self, nums):
        root = None
        if len(nums) == 0:
            return root

        root = TreeNode(nums[0])
        treeNode_list = [root]

        i = 0
        while i < len(nums):
            node = treeNode_list[0]
            del treeNode_list[0]
            ### left child
            i += 1
            if i < len(nums):
                node.left = TreeNode(nums[i])
                treeNode_list.append(node.left)
            ### right child
            i += 1
            if i < len(nums):
                node.right = TreeNode(nums[i])
                treeNode_list.append(node.right)

        return root

def preorder(root):
    if root is not None:
        print ('{} '.format(root.val))
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print ('{} '.format(root.val))
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print ('{} '.format(root.val))

### construct the complete binary tree
root = CompleteBinaryTreeConstructor().construct([1,2,3,4,5,6,7,8,9])

### preorder
print ('preorder')
preorder(root)

### inorder
print ('inorder')
inorder(root)

### postorder
print ('postorder')
postorder(root)
