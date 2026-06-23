class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []

        max_area = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                inx, hei = stack.pop()
                max_area = max(max_area, hei * (index - inx))
                start = inx
            stack.append((start, height))

        for i, h in stack:
            max_area = max(max_area, (h * (len(heights) - i)))

        return max_area 


        