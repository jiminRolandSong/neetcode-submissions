class Solution:

    def checkint(self, number):
        try:
            int(number)
            return True
        except:
            return False

    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:

            if self.checkint(o):
                stack.append(int(o))
            elif o == "+":
                sums = stack[-1] + stack[-2]
                stack.append(sums)
            elif o == 'C':
                stack.pop()
            elif o == 'D':
                muls = stack[-1] * 2
                stack.append(muls)
        
        return sum(stack)
        