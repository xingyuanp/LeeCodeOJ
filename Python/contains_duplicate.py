class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return True
        return False