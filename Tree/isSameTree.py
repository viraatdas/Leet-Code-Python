def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.right)

    return p == None and q == None
        
