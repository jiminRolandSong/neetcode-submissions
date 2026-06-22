from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        teehash = defaultdict(int)

        for i in t:
            teehash[i] += 1
        
        need = len(teehash.keys())

        have = 0

        left = 0

        eshash = defaultdict(int)

        length = len(s) + 1
        result = s
        for right in range(len(s)):
            cur = s[right]
            eshash[cur] += 1

            if cur in teehash and eshash[cur] == teehash[cur]:
                have += 1
            
            print(left, right, need, have)
            while left <= right and need==have:
                print(s[left:right + 1])
                if (right - left + 1) < length:
                    result = s[left:right + 1]
                    length = len(result)
                eshash[s[left]] -= 1
                if s[left] in teehash:
                    print(eshash[s[left]], teehash[s[left]])                                     
                    if eshash[s[left]] < teehash[s[left]]:
                        have -= 1
                left += 1
                

        return "" if length > len(s) else result


        