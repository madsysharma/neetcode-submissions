class Solution:
    def compareCharCounts(self, s: str, t: str) -> bool:
        char_count_s = {}
        char_count_t = {}
        result = False
        for c in s:
            if c not in char_count_s.keys():
                char_count_s[c] = 1
            else:
                char_count_s[c] += 1
        for d in t:
            if d not in char_count_t.keys():
                char_count_t[d] = 1
            else:
                char_count_t[d] += 1
        for ch in t:
            if ch in char_count_s.keys() and char_count_s[ch]==char_count_t[ch]:
                result = True
            else:
                result = False
        return result

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        elif len(s) == len(t):
            if s==t:
                return s
            elif s!=t and self.compareCharCounts(s,t)==False:
                return ""
            elif s!=t and self.compareCharCounts(s,t)==True and len(set(s))==len(set(t)):
                return s
        else:
            result = ""
            char_set = set(t)
            start = 0
            length = len(t)
            end = length
            while end - start < len(s):
                while len(s[start:end])==length or len(s[start:len(s)-start])==length:
                    print("Start is: "+str(start)+" and end is: "+str(end))
                    substr = s[start:end] if end <= len(s) - 1 else s[start:]
                    print("Substring is now: "+substr)
                    if len(set(substr).intersection(char_set))==len(char_set) and self.compareCharCounts(substr,t)==True:
                        print("Substring found is: "+substr)
                        result = substr
                        return result
                    else:
                        start += 1
                        end += 1
                if result == "":
                    length += 1
                    start = 0
                    end = length
                    print("Window size is now: "+str(end))
                
            if len(set(s).intersection(char_set))==len(char_set):
                result = s
            else:
                result = ""
                
            return result 
        