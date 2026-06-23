class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:

        spans = 1
        while len(self.prices) > 0 and self.prices[-1][0] <= price:
            pri, span = self.prices.pop()
            print(pri, span)
            spans += span
        
        self.prices.append((price, spans))
        return spans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)