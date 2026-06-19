from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        counts = defaultdict(list)
        for value, count in freq.items():
            counts[count].append(value)
        

        result = []

        for count in sorted(counts.keys(),reverse=True):
            for value in counts[count]:
                result.append(value)
                if len(result) == k:
                    return result


        