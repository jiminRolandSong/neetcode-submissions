class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        warmer = [0] * (len(temperatures))

        for i, t in enumerate(temperatures):
            if len(stack) < 1:
                stack.append((i, t))
            else:
                index, temp = stack[-1]
                while stack and t > stack[-1][1]:
                    index, temp = stack.pop()
                    warmer[index] = (i - index)
                stack.append((i, t))
                    
                print(stack)
                
        
        return warmer
        