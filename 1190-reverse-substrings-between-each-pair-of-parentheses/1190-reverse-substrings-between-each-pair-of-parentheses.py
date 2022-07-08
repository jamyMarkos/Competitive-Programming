class Solution:
    def reverseParentheses(self, s: str) -> str:
        sstr = ""
        stack = []
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                while stack[-1] != "(":
                    sstr += stack.pop()
                stack.pop()
                for i in sstr:
                    stack.append(i)
                sstr = ""
        return "".join([x for x in stack if x not in ["(",")"]])

                
                