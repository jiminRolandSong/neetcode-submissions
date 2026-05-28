class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        for i in range(len(nums) - k + 1):
            maxnum = max(nums[i:i+k])
            result.append(maxnum)
        
        return result

        