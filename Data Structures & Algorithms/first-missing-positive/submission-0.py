class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.append(0)
        nums.sort()
        numset = set(nums)

        for n in nums:
            if n + 1 > 0 and (n + 1) not in numset:
                return n + 1
        