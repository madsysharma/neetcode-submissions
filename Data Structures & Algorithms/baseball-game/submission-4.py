class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tot = 0
        stack = []

        for o in operations:
            if o not in ["+", "C", "D"]:
                # o is a digit
                val = int(o)
                stack.append(val)
            else:
                if o == "+":
                    v1 = stack.pop() if len(stack) > 0 else 0
                    v2 = stack.pop() if len(stack) > 0 else 0
                    res = v1 + v2
                    stack.append(v2)
                    stack.append(v1)
                    stack.append(res)
                elif o == "D":
                    top = stack[-1] if len(stack) > 0 else 0
                    d = 2 * top
                    stack.append(d)
                elif o == "C":
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        continue
            print(stack)
        return sum(stack)