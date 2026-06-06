class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()

        output = 0

        left = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            length = right - left + 1
            output = max(output, length)

        return output 


        