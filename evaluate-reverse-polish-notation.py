class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in '*/+-':
                stack.append(char)
            else:
                op1 = int(stack.pop())
                op2 = int(stack.pop())

                if char == '+':
                    res = op2 + op1
                elif char == '-':
                    res = op2 - op1
                elif char == '/':
                    res = int(op2 / op1)
                else:
                    res = op2 * op1
                
                stack.append(str(res))

        return int(stack[-1])