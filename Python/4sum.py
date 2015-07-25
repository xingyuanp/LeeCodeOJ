class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = set()
        for a in range(n - 3):
            for b in range(a + 1, n - 2):
                c, d = b + 1, n - 1
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    if s < target:
                        c += 1
                    elif s > target:
                        d -= 1
                    else:
                        result.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
        return list(result)