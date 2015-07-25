class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        s = {}
        for i in range(len(nums)):
            if nums[i] not in s or i - s[nums[i]] > k:
                s[nums[i]] = i
            else:
                return True
        return False