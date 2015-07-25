class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                end = mid
        if nums[start] != target:
            return [-1, -1]
        result = [start]
        end = len(nums) - 1
        while start < end:
            if end - start == 1:
                mid = end
            else:
                mid = (start + end) / 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        result.append(end)
        return result
        