class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==0:
            return 0
        elif len(tokens)==1:
            return int(tokens[0])
        else:
            stack = []
            for t in tokens:
                if t not in ['+','-','*','/']:
                    # Numbers
                    op = int(t)
                    stack.append(op)
                else:
                    if len(stack)>=2:
                        op1 = stack.pop()
                        op2 = stack.pop()
                        if t == '+':
                            stack.append(op1 + op2)
                        elif t == '-':
                            stack.append(op2 - op1)
                        elif t == '*':
                            stack.append(op1 * op2)
                        elif t == '/':
                            stack.append(int(op2 / op1))
            return stack.pop()

        