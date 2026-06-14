import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for xi, yi in points:
            distance = xi ** 2 + yi ** 2
            heapq.heappush(heap, [-distance, xi, yi])
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for distance, xi, yi in heap:
            result.append([xi, yi])
        
        return result

        
        