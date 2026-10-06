class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            stack = []
            for c in s:
                if c in ['(', '{', '[']:
                    stack.append(c)
                else:
                    if len(stack) > 0 and ((stack[-1] == '(' and c == ')') or (stack[-1] == '[' and c == ']') or (stack[-1] == '{' and c == '}')):
                        stack.pop()
                    else:
                        stack.append(c)
            
            if len(stack) == 0:
                return True
            else:
                return False