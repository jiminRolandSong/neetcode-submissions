class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(cap):
            ships = 1
            cur_cap = cap
            for w in weights:
                if cur_cap - w < 0:
                    ships += 1
                    cur_cap = cap
                    if ships > days:
                        return False
                
                cur_cap -= w
            return True
        
        left = max(weights)
        right = sum(weights)

        min_cap = right

        while left < right:
            mid = (left + right) // 2
            print(mid)
            if canShip(mid):
 
                min_cap = min(min_cap, mid)
                right = mid
            else:
                left = mid + 1
        
        return min_cap

                

        