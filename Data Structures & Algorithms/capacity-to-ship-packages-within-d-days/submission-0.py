class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship(cap):
            ships = 1
            curr_cap = cap

            for w in weights:
                if curr_cap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curr_cap = cap
                curr_cap -= w
            
            return True
        
        left = max(weights)
        right = sum(weights)
        min_cap = right

        while left < right:
            mid = (left + right) // 2

            if can_ship(mid):
                min_cap = min(min_cap, mid)
                right = mid
            else:
                left = mid + 1
        
        return min_cap
        