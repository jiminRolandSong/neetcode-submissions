class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)

        if len(numset) < 1:
            return 0

        consecs = 1

        for n in numset:
            length = 1
            if (n-1) not in numset:
                while (n + length) in numset:
                    length += 1
            
            consecs = max(length, consecs)
        
        return consecs

        