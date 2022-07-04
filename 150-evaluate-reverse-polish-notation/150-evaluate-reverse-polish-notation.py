class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        result = int(tokens[0])
        def findResult(op, x, y)->int:
            if i == "+":
                return x + y
            elif i == "-":
                return x - y
            elif i == "*":
                return x * y
            else:
                return int(x / y)
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                arr.append(i)
            else:
                right = int(arr.pop())
                left = int(arr.pop())
                result = findResult(i, left, right)
                arr.append(result)
        return result
        