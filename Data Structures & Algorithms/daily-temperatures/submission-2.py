class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)

        warmer = [0] * n

        stack = []

        for cur_i, cur_t in enumerate(temperatures):

            if len(stack) < 1:
                stack.append((cur_i, cur_t))
            else:
                while stack and stack[-1][1] < cur_t:
                    index = stack[-1][0]
                    warmer[index] = cur_i - index
                    stack.pop()
                
                stack.append((cur_i, cur_t))
            
        return warmer


        