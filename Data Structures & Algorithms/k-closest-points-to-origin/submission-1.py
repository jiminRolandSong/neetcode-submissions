import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dists = []
        heapq.heapify(dists)

        for xi, yi in points:
            distance = xi ** 2 + yi ** 2
            heapq.heappush(dists, [-distance, xi, yi])
            if len(dists) > k:
                heapq.heappop(dists)

        result = []
        for distance, xi, yi in dists:
            result.append([xi, yi])
        
        return result


        