class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        m = matrix
        n = len(m)
        for i in range(n / 2):
            for j in range((n + 1) / 2):
                m[i][j], m[j][n-1-i], m[n-1-i][n-1-j], m[n-1-j][i] = m[n-1-j][i], m[i][j], m[j][n-1-i], m[n-1-i][n-1-j]
        