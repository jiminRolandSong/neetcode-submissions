class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = -heapq.heappop(self.large)
            heapq.heappush(self.small, val)
        
        print(self.small)
        print(self.large)
        

    def findMedian(self) -> float:
        if self.small and self.large:
            smax = -self.small[0]
            lmin = self.large[0]
            if len(self.small) == len(self.large):
                return (smax + lmin) / 2
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.small) < len(self.large):
            return self.large[0]
        
        return 0.0
        
        
        