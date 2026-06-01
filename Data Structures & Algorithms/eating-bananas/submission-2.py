from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lowspeed = 1
        highspeed = max(piles)
        minrate = highspeed

        while lowspeed < highspeed:
            print(lowspeed, highspeed)
            midspeed = (lowspeed + highspeed) // 2

            totalH = 0

            for p in piles:
                totalH += ceil(float(p) / midspeed) 
            
            if totalH > h:
                lowspeed = midspeed + 1
                
            elif totalH <= h:
                minrate = midspeed
                highspeed = minrate
        
        return minrate



        