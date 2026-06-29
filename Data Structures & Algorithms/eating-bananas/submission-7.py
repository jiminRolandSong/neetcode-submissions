from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        min_rate = right

        while left < right:
            mid = (left + right) // 2

            total_time = 0  

            for p in piles:
                total_time += ceil(float(p) / mid)
            
            if total_time <= h:
                min_rate = min(min_rate, mid)
                right = mid
            else:
                left = mid + 1
                
        
        return min_rate



        