import heapq
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.append(0)
        numset = set(nums)
        
        heapq.heapify(nums)
        while nums:
            number = heapq.heappop(nums)
            if number + 1 not in numset and number + 1 > 0:
                return number + 1
        