def isValid(s):
    def match(c1, c2):
        case1 = ( c1 == '(' and c2 == ')' )
        case2 = ( c1 == '[' and c2 == ']' )
        case3 = ( c1 == '{' and c2 == '}' )
        return case1 or case2 or case3

    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif len(stack) > 0 and match(stack[-1], c):
            stack.pop()
        else:
            return False
    return stack == []
                