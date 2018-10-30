def binaryTreePaths(root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        treepath = [str(root.val) + "->" + path for path in self.binaryTreePaths(root.left)]
        treepath += [str(root.val) + "->" + path for path in self.binaryTreePaths(root.right)]

        return treepath
