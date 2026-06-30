class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(subsum):
            subarrays = 1
            current_sum = 0
            for n in nums:
                current_sum += n
                if current_sum > subsum:
                    subarrays += 1
                    if subarrays > k:
                        return False
                    current_sum = n
            return True
                
        
        left = max(nums)
        right = sum(nums)
        min_sum = right

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                min_sum = min(min_sum, mid)
                right = mid
            else:
                left = mid + 1
        
        return min_sum


        