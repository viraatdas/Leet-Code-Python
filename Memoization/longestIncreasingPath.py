def longestIncreasingPath(self, matrix):
    def dfs(i, j):
        if not 

    if not matrix or not matrix[0]:
        return 0 

    M = len(matrix)
    N = len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return 
