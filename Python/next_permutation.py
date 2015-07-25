class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0:
            j = i + 1
            while j < len(nums):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    return
                j += 1
            for j in range(i, len(nums) - 1):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            i -= 1
