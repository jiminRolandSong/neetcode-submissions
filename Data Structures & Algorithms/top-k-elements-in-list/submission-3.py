from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = defaultdict(int)

        for i in nums:
            freqs[i] += 1
        
        bucket = defaultdict(list)

        for key, value in freqs.items():
            bucket[value].append(key)
        
        result = []

        for key in sorted(bucket.keys(), reverse = True):
            for num in bucket[key]:
                result.append(num)
            
            if len(result) == k:
                return result
        
        return result
            
        