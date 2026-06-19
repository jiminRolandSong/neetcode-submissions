from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        numset = set(nums)

        for n in nums:
            counts[n] += 1
        
        result = []

        for n in numset:
            if counts[n] > (len(nums)/3):
                result.append(n)

        return result        