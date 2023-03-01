class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                str_ = ''
                while stack and stack[-1] != '[':
                    str_ = stack.pop() + str_

                if stack: stack.pop()

                times = ''

                while stack and stack[-1].isnumeric():
                    times = stack.pop() + times

                newStr = str_ * int(times)

                for char in newStr:
                    stack.append(char)

        if stack[-1].isnumeric():
            return ''

        return ''.join(stack)