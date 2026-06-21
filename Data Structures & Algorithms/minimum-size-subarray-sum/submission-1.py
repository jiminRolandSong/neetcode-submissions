class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0

        minlen = len(nums) + 1

        sum = 0
        while right < len(nums):    
            sum += nums[right]
            if sum >= target:
                while sum >= target and left <= right:
                    minlen = min(right - left + 1, minlen)
                    sum -= nums[left]
                    left += 1         
            print(left, right, sum)
            
            right += 1
        
        return 0 if minlen > len(nums) else minlen