from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        indices = defaultdict(int)
        for i in range(len(nums)):
            number= nums[i]
            if number in indices and abs(i - indices[number] <= k):
                return True
            indices[number] = i
        
        return False

        