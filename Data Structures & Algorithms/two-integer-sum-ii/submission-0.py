class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0
        end = len(numbers) - 1

        result = []

        for i in range(len(numbers)):
            added = numbers[start] + numbers[end]

            if added == target:
                result.append(start + 1)
                result.append(end + 1)
                return result
            
            if added > target:
                end -= 1
            else:
                start += 1
            

        