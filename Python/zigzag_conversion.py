def convert(s, nRows): 
    if nRows == 1:
        return s
        
    rowList = ['' for i in range(nRows)]
    period = 2 * nRows - 2
    count = 0
    for c in s:
        r = count % period
        row = min(r, period - r)
        rowList[row] += c
        count += 1
    
    result = ''
    for i in range(nRows):
        result += rowList[i]
    
    return result
