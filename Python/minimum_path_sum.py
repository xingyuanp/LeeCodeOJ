class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        d = [n * [0] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    d[i][j] = grid[i][j]
                elif i == 0:
                    d[i][j] = d[i][j - 1] + grid[i][j]
                elif j == 0:
                    d[i][j] = d[i - 1][j] + grid[i][j]
                else:
                    d[i][j] = min(d[i - 1][j], d[i][j - 1]) + grid[i][j]
        return d[-1][-1]