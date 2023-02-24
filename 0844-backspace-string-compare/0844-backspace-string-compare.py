class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        
        def corrStr(s: str) -> str:
            for char in s:
                if char != '#':
                    stack.append(char)
                else:
                    if len(stack):
                        stack.pop()
                    
            return ''.join(stack)
        s = corrStr(s)
        stack.clear()
        t = corrStr(t)
        
        return s == t
        
        
        