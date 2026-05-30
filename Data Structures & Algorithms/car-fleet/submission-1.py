class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        for p, s in sorted(zip(position,speed), reverse = True):
            time = (target - p) / s
            if not stack:
                stack.append(time)
            else:
                top_time = stack[-1]
                if top_time < time:
                    stack.append(time)
                       
                
        return len(stack)