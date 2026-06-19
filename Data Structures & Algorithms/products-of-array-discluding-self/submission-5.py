class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = [1] * len(nums)

        prev = 1
        for n in range(len(nums)):
            products[n] = products[n] * prev
            prev = prev * nums[n]
        
        prev = 1
        for n in range(len(nums) - 1, -1, -1):
            products[n] *= prev
            prev = prev * nums[n]
        
        return products
        