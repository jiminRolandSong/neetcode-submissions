class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums) < 1:
            return 0

        nums.sort()
        maxnum = max(nums) + 1
        n = len(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = maxnum + 1
                count += 1
        nums.sort()

        return n - count
        