class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        result = '0'
        for i in reversed(range(len(num1))):
            term = (len(num1) - 1 - i) * '0'
            carry = 0
            for j in reversed(range(len(num2))):
                p = int(num1[i]) * int(num2[j]) + carry
                term = str(p % 10) + term
                carry = p / 10
            if carry > 0:
                term = str(carry) + term
            temp_result = result[len(result) - (len(num1) - 1 - i):]
            carry = 0
            for k1 in reversed(range(len(result) - (len(num1) - 1 - i))):
                k2 = len(term) - len(result) + k1
                s = int(result[k1]) + int(term[k2]) + carry
                temp_result = str(s % 10) + temp_result
                carry = s / 10
            for k2 in reversed(range(len(term) - len(result))):
                s = int(term[k2]) + carry
                temp_result = str(s % 10) + temp_result
                carry = s / 10
            if carry > 0:
                temp_result = str(carry) + temp_result
            result = temp_result
        return result