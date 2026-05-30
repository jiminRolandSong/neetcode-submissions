class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = []

        for n in nums:
            product.append(1)


        # product of numbers in the left
        left = 1

        for l in range(len(nums)):
            product[l] = product[l] * left
            left = left * nums[l]
        
        # product of numbers in the right
        right = 1

        for r in range(len(nums) -1, -1, -1):
            product[r] = product[r] * right
            right = right * nums[r]
        
        return product
        
        