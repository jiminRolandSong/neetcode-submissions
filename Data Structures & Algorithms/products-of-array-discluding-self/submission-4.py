class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

    
        n = len(nums)

        products = [1] * n
        left = 1
        for i in range(n):
            products[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(n-1, -1, -1):
            products[i] *= right
            right *= nums[i]
            
        
        
        return products


        