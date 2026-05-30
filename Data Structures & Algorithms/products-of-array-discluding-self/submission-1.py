class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        

        n = len(nums)

        prefix = [1] * n
        left = 1
        for i in range(n):
            prefix[i] = left
            left *= nums[i]
        
        suffix = [1] * n
        right = 1

        for i in range(n-1, -1, -1):
            suffix[i] = right
            right *= nums[i]
        
        output = [1] * n

        print(suffix)
        print(prefix)

        for i in range(n):
            output[i] = prefix[i] * suffix[i]
        
        return output


        