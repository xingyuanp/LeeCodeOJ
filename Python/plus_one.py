def plusOne(digits):
    ans = digits[:]
    for i in reversed(range(len(digits))):
        if digits[i] != 9:
            ans[i] += 1
            break
        else:
            ans[i] = 0
    else:
        ans = [1] + ans
    return ans