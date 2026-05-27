class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        length = 0

        substring = []
        for i in range(len(s)):
            if s[i] not in substring:
                substring.append(s[i])
            else:
                find = substring.index(s[i])
                #substring.pop(find)
                substring = substring[find+1:]
                substring.append(s[i])

            length = max(length, len(substring))
        
        return length


        