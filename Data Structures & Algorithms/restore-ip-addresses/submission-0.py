class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValidSegment(ip):
            if not str.isnumeric(ip) or len(ip) > 3:
                return False
            elif int(ip) not in range(0, 256) or (len(ip) > 1 and ip[0] == "0"):
                return False
            
            return True

        results = []

        def backtrack(start, rem_dots, curr_path):
            if rem_dots == 0:
                curr_seg = s[start:]
                if isValidSegment(curr_seg):
                    results.append(curr_path + curr_seg)
                return
            for i in range(1, 4):
                if start + i < len(s):
                    curr_seg = s[start:start+i]
                    if isValidSegment(curr_seg):
                        backtrack(start + i, rem_dots - 1, curr_path + curr_seg + ".")

        backtrack(0, 3, "")
        return results
