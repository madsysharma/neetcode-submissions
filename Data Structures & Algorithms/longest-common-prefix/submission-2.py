class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        i = 0
        min_len = min([len(s) for s in strs])
        while i < min_len:
            char_list = [s[i] for s in strs]
            if len(set(char_list)) == 1:
                lcp += char_list[0]
                i += 1
            else:
                break
        return lcp