from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()
        connections = defaultdict(list)

        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for c in connections[node]:
                dfs(c)
        
        count = 0
        for node in connections:
            if node not in visited:
                dfs(node)
                count += 1
        
        return count + (n - len(connections))
            
        