class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        length = 0
        result = 0
        for r in range(len(s)):
            if s[r] in char_map:
                length = max(char_map[s[r]] + 1, length)
            char_map[s[r]] = r
            result = max(result, r - length + 1)
        return result
                
