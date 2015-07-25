class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums_copy = nums[:]
        for i in range(n):
            nums[(i + k) % n] = nums_copy[i]