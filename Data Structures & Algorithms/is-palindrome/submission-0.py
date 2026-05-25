class Solution:
    def isPalindrome(self, s: str) -> bool:

        checks = "".join(char for char in s if char.isalnum())
        stringlen = len(checks)

        for i in range(stringlen):
            if checks[i].lower() != checks[stringlen - 1 - i].lower():
                return False
        
        return True
        