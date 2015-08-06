class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        result = [n * [0] for row in range(n)]
        i, j = 0, 0
        di, dj = 0, 1
        for num in range(1, n * n + 1):
            result[i][j] = num
            try:
                assert result[i + di][j + dj] == 0
            except (IndexError, AssertionError):
                di, dj = dj, -di
            i, j = i + di, j + dj
        return result