class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        triangle = self.generate(numRows - 1)
        last_row = triangle[-1]
        newRow = [1]
        for i in range(1, len(last_row)):
            newRow.append(last_row[i - 1] + last_row[i])
        newRow.append(1)
        triangle.append(newRow)
        return triangle