class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)

        warmer = [0] * n

        stack = []

        for i, t in enumerate(temperatures):

            if len(stack) < 1:
                stack.append((i, t))
            else:

                while stack and stack[-1][1] < t:
                    index = stack[-1][0]
                    warmer[index] = i - index
                    stack.pop()
                
                stack.append((i, t))
            
        return warmer
        