from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        result = 0
        currentsum = 0
        prefixsum = defaultdict(int)
        prefixsum[0] = 1

        for n in nums:
            currentsum += n
            diff = currentsum - k

            result += prefixsum[diff]
            prefixsum[currentsum] += 1
        
        return result


        