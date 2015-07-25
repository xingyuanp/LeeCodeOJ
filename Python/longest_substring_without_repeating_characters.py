class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        length = 0
        char_set = set()
        i = j = 0
        while i < len(s) and j < len(s):
            if s[j] in char_set:
                length = max(length, j - i)
                char_set.remove(s[i])
                i += 1
            else:
                char_set.add(s[j])
                j += 1
        return max(length, j - i)
