class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ['+', '-', '*', '/']

        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                second = stack.pop()
                first = stack.pop()

                if t == '+':
                    stack.append(first + second)
                elif t == '-':
                    stack.append(first - second)
                elif t == '*':
                    stack.append(first * second)
                elif t == '/':
                    stack.append(int(first / second))
        
        return stack[-1]