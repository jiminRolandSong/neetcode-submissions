class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concated = [0] * (2 * n)
        for i in range(n):
            concated[i] = concated[i + n] = nums[i]
        
        return concated
        