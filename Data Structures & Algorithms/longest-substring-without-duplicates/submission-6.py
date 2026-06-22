class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substring = []

        result = 0

        left = 0

        for i in range(len(s)):
            if s[i] in substring:
                index = substring.index(s[i])
                substring = substring[index + 1:]
                substring.append(s[i])
            else:
                substring.append(s[i])

            result = max(len(substring), result)
        
        return result
            

        