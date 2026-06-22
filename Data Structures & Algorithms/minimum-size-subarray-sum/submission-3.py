class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0

        min_len = len(nums) + 1
        current_sum = 0

        for right in range(len(nums)):
            value = nums[right]
            current_sum += value
            print(current_sum)
            while left <= right and current_sum >= target:
                min_len = min(right - left + 1, min_len)
                current_sum -= nums[left]
                left += 1
            
            
        
        return 0 if min_len > len(nums) else min_len

        