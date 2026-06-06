class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []

        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                total = nums[start] + nums[end] + nums[i]

                if total == 0:

                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    
                    final = [nums[i], nums[start], nums[end]]

                    if final not in result:
                        result.append(final)
                    
                    start += 1
                    end -= 1
                elif total > 0:
                    end -= 1
                elif total < 0:
                    start += 1
        
        return result
                
        