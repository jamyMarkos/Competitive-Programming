class StockSpanner:

    def __init__(self):
        self.stack = []
        self.ans = [1]
        

    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1] <= price:
            count += self.ans[-1]
            self.ans.pop()
            self.stack.pop()
        self.ans.append(count)
        self.stack.append(price)

        return self.ans[-1]  
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)