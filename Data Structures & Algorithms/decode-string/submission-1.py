class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                substring = ""
                while stack and stack[-1] !='[':
                    now = stack.pop()
                    substring = now + substring
                stack.pop()
                
                counts = 0
                tennum = 0
                while stack and stack[-1].isdigit():
                    num = stack.pop()
                    counts = (int(num) * (10 ** tennum)) + counts
                    tennum += 1


                stack.append(substring * counts)


        return "".join(stack)

        