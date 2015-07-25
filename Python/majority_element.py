class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        c = {}
        for num in nums:
            c[num] = 0
        for num in nums:
            c[num] += 1
        result = None
        for num in c:
            if result == None or c[num] > c[result]:
                result = num
        return result