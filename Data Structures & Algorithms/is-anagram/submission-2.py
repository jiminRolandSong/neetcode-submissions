class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        sos = sorted(s)
        sot = sorted(t)
        
        for i in range(len(sos)):
            if sos[i] != sot[i]:
                return False
        
        return True
        