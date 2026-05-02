class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return False
        else:
            stack = []
            top = len(stack) - 1
            match_dict = {'(':')', '{':'}', '[':']'}
            full_string_processed = True
            result = False
            for ch in s:
                if ch in ['(', '[', '{']:
                    stack.append(ch)
                elif ch in [')', '}', ']']:
                    if len(stack)==0:
                        full_string_processed = False
                        break
                    elif len(stack)!=0 and match_dict[stack[top]]==ch:
                        stack.pop()
                    elif len(stack)!=0 and match_dict[stack[top]]!=ch:
                        full_string_processed = False
                        break
            if len(stack)==0 and full_string_processed==True:
                result = True
            else:
                result = False
            return result
        