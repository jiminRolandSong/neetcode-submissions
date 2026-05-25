class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start = 0
        end = len(heights) - 1

        maxarea = 0

        while start < end:
            water = (end - start) * min (heights[start], heights[end])

            maxarea = max(maxarea, water)

            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        
        return maxarea
        