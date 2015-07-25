class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
    	roman = ''

    	roman += num / 1000 * 'M'

    	num %= 1000
    	if num >= 900:
    		roman += 'CM'
    	elif num >= 500:
    		roman += 'D' + (num - 500) / 100 * 'C'
    	elif num >= 400:
    		roman += 'CD'
    	else:
    		roman += num / 100 * 'C'

    	num %= 100
    	if num >= 90:
    		roman += 'XC'
    	elif num >= 50:
    		roman += 'L' + (num - 50) / 10 * 'X'
    	elif num >= 40:
    		roman += 'XL'
    	else:
    		roman += num / 10 * 'X'

    	num %= 10
    	if num >= 9:
    		roman += 'IX'
    	elif num >= 5:
    		roman += 'V' + (num - 5) * 'I'
    	elif num >= 4:
    		roman += 'IV'
    	else:
    		roman += num * 'I'

    	return roman