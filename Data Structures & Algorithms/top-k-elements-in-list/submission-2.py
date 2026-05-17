from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numsdict = defaultdict(int)

        for n in nums:
            numsdict[n] +=1
        
        bucket = defaultdict(list)

        for num, freq in numsdict.items():
            bucket[freq].append(num)
        
        output = []

        for f in sorted(bucket.keys(), reverse = True):
            for i in bucket[f]:
                output.append(i)

            if len(output) == k:
                return output 


        return []