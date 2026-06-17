from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n-1):
            return False

        connections = defaultdict(list)

        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)
        
        cycle = set()
        visited = set()

        def dfs(node, pair):
            if node in visited:
                return True
            
            if node in cycle:
                return False
            
            cycle.add(node)
            for c in connections[node]:
                if c == pair:
                    continue
                if not dfs(c, node):
                    return False
            cycle.remove(node)
            visited.add(node)
            return True
        
        return dfs(0, -1) and len(visited) == n
            

            



        