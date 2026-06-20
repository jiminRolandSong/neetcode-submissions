class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        result = []
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                c = b + 1
                d = len(nums) - 1       
                while c < d:
                    anum = nums[a]
                    bnum = nums[b]
                    cnum = nums[c]
                    dnum = nums[d]
                    total = anum + bnum + cnum + dnum

                    if total == target:

                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        
                        while c < d and nums[d] == nums[d-1]:
                            d -= 1
                        
                        final = [anum, bnum, nums[c], nums[d]]
                        if final not in result:
                            result.append(final)
                        
                        c += 1
                        d -= 1
                    elif total < target:
                        c += 1
                    else:
                        d -= 1
        
        return result
                        
        