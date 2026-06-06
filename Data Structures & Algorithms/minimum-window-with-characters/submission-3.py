from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        teehash = defaultdict(int)

        for c in t:
            teehash[c] += 1
        
        need = len(teehash)

        have = 0
        start = 0

        result = ""

        swindow = defaultdict(int)

        for end in range(len(s)):
            swindow[s[end]] += 1

            if s[end] in teehash and swindow[s[end]] == teehash[s[end]]:
                have += 1
            
            while need == have:
                substring = s[start: end + 1]

                if result == "" or len(substring) < len(result):
                    result = substring
                
                swindow[s[start]] -= 1
                if s[start] in teehash and swindow[s[start]] < teehash[s[start]]:
                    have -= 1
                
                start += 1
        return result

        