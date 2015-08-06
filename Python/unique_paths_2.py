class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        d = [n * [0] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    d[i][j] = 0
                elif i == j == 0:
                    d[i][j] = 1
                elif i == 0:
                    d[i][j] = d[i][j - 1]
                elif j == 0:
                    d[i][j] = d[i - 1][j]
                else:
                    d[i][j] = d[i - 1][j] + d[i][j - 1]
        return d[-1][-1]