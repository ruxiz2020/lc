class StockSpanner:

    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        day = 1
        while self.stack and self.stack[-1][0] <= price:
            day += self.stack.pop()[1]
        self.stack.append((price, day))
        return day

# Your StockSpanner object will be instantiated and called as such:
S = StockSpanner()
res = S.next(100) #is called and returns 1,
print(res)
S.next(80) #is called and returns 1,
S.next(60) #is called and returns 1,
S.next(70) #is called and returns 2,
S.next(60) #is called and returns 1,
S.next(75) #is called and returns 4,
res = S.next(85) #is called and returns 6.
print(res)
