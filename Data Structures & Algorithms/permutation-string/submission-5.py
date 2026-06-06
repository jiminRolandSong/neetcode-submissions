from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        start = 0

        freq1 = defaultdict(int)

        for i in s1:
            freq1[i] += 1
        
        
        for s in range(len(s2) - len(s1) + 1):
            cur_window = s2[s: s + len(s1)]
            check = True
            for key, value in freq1.items():
                if cur_window.count(key) != value:                   
                    check = False
            if check:
                return True
        
        return False
        