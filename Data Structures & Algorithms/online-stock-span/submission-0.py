class StockSpanner:

    def __init__(self):
        self.st = [] # Each entry is (price, gap)

    def next(self, price: int) -> int:
        gap = 1
        while self.st and self.st[-1][0] <= price:
            gap += self.st[-1][1]
            self.st.pop()
        self.st.append((price, gap))
        return gap


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)