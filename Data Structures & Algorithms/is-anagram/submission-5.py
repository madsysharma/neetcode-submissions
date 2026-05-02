class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      elif len(s)==len(t) and len(set(s).intersection(set(t))) < len(set(s)):
        return False
      else:
        res = False
        char_dict={}
        for i in range(0, len(s)):
            if s[i] not in char_dict.keys():
                char_dict[s[i]] = 1
            else:
                char_dict[s[i]] += 1
            if t[i] not in char_dict.keys():
                char_dict[t[i]] = 1
            else:
                char_dict[t[i]] += 1
        print(char_dict)
        for v in char_dict.values():
            if v%2 == 0:
                res = True
            else:
                res = False
        return res