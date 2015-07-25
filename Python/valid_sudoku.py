def isValidSudoku(board):
    def isValid(a):
        """
        a: a list of length 9
        return: boolean
        """
        digits = '123456789'
        d = {}
        for c in a:
            if c in digits:
                if c not in d:
                    d[c] = 1
                else:
                    return False
            elif c != '.':
                return False
        return True
    
    for row in range(9):
        if not isValid(board[row]):
            return False
    
    for column in range(9):
        a = []
        for row in range(9):
            a.append(board[row][column])
        if not isValid(a):
            return False
    
    for i in range(3):
        for j in range(3):
            a = [board[3*i][3*j], board[3*i][3*j+1], board[3*i][3*j+2],
                 board[3*i+1][3*j], board[3*i+1][3*j+1], board[3*i+1][3*j+2],
                 board[3*i+2][3*j], board[3*i+2][3*j+1], board[3*i+2][3*j+2]]
            if not isValid(a):
                return False
    
    return True