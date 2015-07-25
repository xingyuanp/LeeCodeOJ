class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        d = {}
        result = []
        for s in strs:
            key = tuple(sorted(s))
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)
        for key in d:
            if len(d[key]) > 1:
                result.extend(d[key])
        return result