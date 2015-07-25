class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        row = []
        for i in range(rowIndex):
            temp = row[:]
            row = [1]
            for j in range(1, len(temp)):
                row.append(temp[j - 1] + temp[j])
            row.append(1)
        return row