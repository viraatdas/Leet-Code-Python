def zigzagLevelOrder(self, root):
    if not root:
        return []
    res = []
    temp = []
    stack = [root]
    flag = 1
    
    #BFS solution
    while stack:
        for i in range(len(stack)):
            node = stack.pop(0)
            temp+=[node.val]
            if node.left: #node.left not None
                stack+=[node.left]
            if node.right:
                stack+=[node.right]

        res+=[temp[::flag]] #flag determines if appending to res in the right or left order
        temp = [] 
        flag*=-1

    return res
