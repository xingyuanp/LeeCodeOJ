class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        def comb(candidates, target):
            if len(candidates) == 0:
                if target == 0:
                    return set([tuple()])
                return set()
            
            last = candidates[-1]
            result = comb(candidates[:-1], target)
            if last <= target:
                partial = comb(candidates[:-1], target - last)
                for combination_tuple in partial:
                    combination_list = list(combination_tuple)
                    combination_list.append(last)
                    result.add(tuple(combination_list))
            return result
        
        candidates.sort()
        return [list(c) for c in comb(candidates, target)]