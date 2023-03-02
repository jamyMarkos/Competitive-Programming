class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if stack[-1].isdigit():
                    tmp = int(stack.pop()) * 2
                    stack.pop()

                    if stack and stack[-1].isdigit():
                        stack.append(str(tmp + int(stack.pop())))
                    else:
                        stack.append(str(tmp))

                else:
                    stack.pop()
                    if stack and stack[-1].isdigit():
                        stack.append(str(1 + int(stack.pop())))
                    else:
                        stack.append(str(1))

        return int(stack[-1])