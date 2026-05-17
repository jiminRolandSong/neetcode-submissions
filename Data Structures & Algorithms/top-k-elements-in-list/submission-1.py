from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numset = set(nums)

        numsdict = defaultdict(list)

        for n in numset:
            counts = nums.count(n)
            numsdict[counts].append(n)
        
        sortf = sorted(numsdict.keys(), reverse = True)

        sortf = sortf[:k]

        output = []

        for s in sortf:
            for n in numsdict[s]:
                output.append(n)
        
        return output[:k]


        