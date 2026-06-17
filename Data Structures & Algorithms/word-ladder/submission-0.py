from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordset = set(wordList)
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        while q:
            word, steps = q.popleft()

            visited.add(word)
            
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for s in "qwertyuiopasdfghjklzxcvbnm":
                    new_word = word[:i] + s + word[i+1:]
                    if new_word in wordList and new_word not in visited:
                        q.append((new_word, steps+1))
        
        return 0

        