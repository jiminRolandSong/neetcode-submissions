class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        area = 0

        for i in range(len(heights)):
            if len(stack) < 1:
                stack.append((i, heights[i]))
            
            else:
                while stack and heights[i] < stack[-1][1]:
                    index, height = stack.pop()
                    left = 0 if not stack else stack[-1][0] + 1
                    area = max(area, (i - left) * height)

                stack.append((i, heights[i]))

        
        while stack:
            index, height = stack.pop()
            left = 0 if not stack else stack[-1][0] + 1
            area = max(area, height * (len(heights) - left))
        
        return area

        

                
        