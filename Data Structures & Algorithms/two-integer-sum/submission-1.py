from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if nums[i] in numdict.keys():
                return [numdict[nums[i]], i]
            else:
                
                numdict[difference] = i
                print(numdict)
        
        return []