class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        isClosed = True
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            elif len(stack) > 0 :
                if stack[-1] == "(" and i == ")":
                    stack.pop()
                elif stack[-1] == "[" and i == "]":
                    stack.pop()
                elif stack[-1] == "{" and i == "}":
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return isClosed

                
        