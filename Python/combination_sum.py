class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        def comb(candidates, target):
        	"""Helper function assumes candidates sorted"""

        	# Base case
        	if len(candidates) == 0:
        		if target == 0:
        			return [[]]
        		return []

        	result = []
        	last = candidates[-1]
        	n = target / last
        	for i in range(n + 1):
        		partial = comb(candidates[:-1], target - i * last)
        		for c in partial:
        			c.extend(i * [last])
        		result.extend(partial)
        	return result

        candidates.sort()
        return comb(candidates, target)