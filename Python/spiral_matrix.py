class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        
        result = []
        while True:
            result.extend(matrix.pop(0))
            if len(matrix) == 0:
                break
            m, n = len(matrix), len(matrix[0])
            matrix = [[matrix[i][j] for i in range(m)] for j in reversed(range(n))]
        
        return result