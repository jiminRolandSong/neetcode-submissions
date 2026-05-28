from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = defaultdict(int)

        for i in t:
            need[i] += 1
        
        have = 0
        total = len(need)
        
        start = 0
        result = ""

        window = defaultdict(int)

        for end in range(len(s)):
            window[s[end]] += 1

            if s[end] in need and window[s[end]] == need[s[end]]:
                have += 1
            
            while have == total:
                if result == "" or end-start+1 < len(result):
                    result = s[start:end+1]
                
                window[s[start]] -= 1
                if s[start] in need and window[s[start]] < need[s[start]]:
                    have -= 1
                start += 1
            
        
        return result
            


        