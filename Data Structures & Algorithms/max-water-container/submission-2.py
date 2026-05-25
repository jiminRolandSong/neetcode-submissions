class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start = 0
        end = len(heights) - 1

        maxarea = 0

        for i in range(len(heights)):
            water = (end - start) * min (heights[start], heights[end])

            maxarea = max(maxarea, water)

            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        
        return maxarea
        