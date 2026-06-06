class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        output = 0
        substring = []

        for i in range(len(s)):
            if s[i] not in substring:
                substring.append(s[i])
            else:
                index = substring.index(s[i])
                substring = substring[index+1:]
                substring.append(s[i])
            
            output = max(len(substring), output)
        
        return output




        