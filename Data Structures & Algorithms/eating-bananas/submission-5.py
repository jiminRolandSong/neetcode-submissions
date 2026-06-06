from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        low = 1
        high = max(piles)

        speed = high

        while low < high:
            mid = (low + high) // 2

            total = 0

            for p in piles:
                total += ceil(float(p) / mid)
            
            if total <= h:
                speed = min(speed, mid)
                high = mid
            else:
                low = mid + 1
        
        return speed
        