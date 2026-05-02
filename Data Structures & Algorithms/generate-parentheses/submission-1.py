import math
class Solution:
    def isWellFormed(self, s: str) -> bool:
        if len(s)==0:
            return False
        else:
            stack = []
            full_string_checked = True
            for c in s:
                if c=='(':
                    stack.append(c)
                elif c==')':
                    if len(stack)==0:
                        full_string_checked = False
                        break
                    elif len(stack)!=0 and stack[-1]=='(':
                        stack.pop()
                    else:
                        full_string_checked = False
                        break
            if len(stack)==0 and full_string_checked==True:
                return True
            else:
                return False



    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return [""]
        else:
            p_dict = {"(":")"}
            results = []
            upper_limit = (2*n)+1
            start_limit = 2 ** ((2*n)-1)
            end_limit = (2 ** upper_limit) - 1
            for nc in range(start_limit, end_limit):
                b_str = str(bin(nc))
                b_str = b_str.replace("0b", "")
                b_str = b_str.replace("1","(")
                b_str = b_str.replace("0",")")
                if len(b_str)==2*n and self.isWellFormed(b_str)==True:
                    results.append(b_str)
            return results
                
            
            
            

