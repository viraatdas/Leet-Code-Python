# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#recursively
def inorderTraversal(self, root):
    appList = []
    self.append(root, appList)
    return appList

def helper(self, root, appList):
    if root:
        self.helper(root.left, appList)
        appList.append(root.val)
        self.helper(root.right, appList)


#iteratively
def inorderTraversal(self, root):
    res = []
    stack  []
    while True:
        while root:
            stack.append(root)
            root = root.left

        if not stack: #if stack is empty return res. This will go through after a certain iteration of stack. pop()
            return stack 

        node = stack.pop() #the stack list is [root, root.left, root.left.left,...                         
                         #node variable has the last root which is the bottom-leftmost value (first iteration)
        res.append(node.val)
        root = node.right 
        
