class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2:
            return False

        stack = []

        for i in range(len(s)):
            if s[i] in ['[', '{', '(']:
                stack.append(s[i])

            else:

                if len(stack) < 1:
                    return False
                popped = stack[-1]
                print(popped)               
                cha = s[i]              
                if popped == '{' and cha != '}':
                    return False
                elif popped == '[' and cha != ']':
                    return False
                elif popped == '(' and cha != ')':
                    return False

                stack.pop()



        
        return len(stack) == 0
        