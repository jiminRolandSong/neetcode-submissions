from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        start = 1
        end = max(piles)

        speed = end

        while start < end:

            mid = (start + end) // 2

            time = 0

            for p in piles:
                time += ceil(float(p) / mid)
            
            if time <= h:
                speed = min(speed, mid)
                end = mid
            else:
                start = mid + 1
        
        return speed

        