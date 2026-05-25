class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while end > start:
                added = nums[start] + nums[end] + nums[i]
                if added == 0 and start != i and end != i:
                    numslists = [nums[i], nums[start], nums[end]]
                    if numslists not in result:
                        result.append(numslists)
                    start += 1
                    end -= 1
                elif added > 0:
                    end -= 1
                else:
                    start += 1
        
        return result

            


        