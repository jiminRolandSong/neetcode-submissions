from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
 
        counts = defaultdict(int)
        n = len(s1)
        for s in s1:
            counts[s] += 1


        for i in range(len(s2) - n + 1):
            sub = s2[i: i + n]
            print(sub)
            check = True

            for key, value in counts.items():
                if value != sub.count(key):
                    check = False
            
            if check:
                return True
        
        return False
        