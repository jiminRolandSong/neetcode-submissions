class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            new_area = (right - left) * min(heights[left], heights[right])
            area = max(area, new_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return area
            