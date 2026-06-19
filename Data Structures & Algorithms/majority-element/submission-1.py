from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        for key in sorted(counts.keys()):
            if counts[key] > len(nums) / 2:
                return key
        