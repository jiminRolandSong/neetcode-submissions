from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        first = defaultdict(int)

        for s in s1:
            first[s] += 1
        
        for i in range(len(s2) - len(s1) + 1):
            sub = s2[i: i + len(s1)]

            check = True
            for key, value in first.items():
                if sub.count(key) != value:
                    check = False
            
            if check:
                return True
        
        return False

        