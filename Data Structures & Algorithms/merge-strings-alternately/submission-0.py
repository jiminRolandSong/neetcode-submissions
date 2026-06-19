class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        merged = ""
        while index < len(word1) and index < len(word2):
            merged += word1[index]
            merged += word2[index]
            index += 1
        
        print(index)
        if index < len(word1):
            merged += word1[index:]
        else:
            merged += word2[index:]
        
        return merged
        