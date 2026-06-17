from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        connections = defaultdict(list)

        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)
        
        visited = set()
        cycle = set()
        
        remove = set()
        def dfs(node, pair):
            if node in visited:
                return True
            
            if node in cycle:
                print(node, pair)
                return False
            
            cycle.add(node)

            for c in connections[node]:
                print(node, connections[node], pair)
                if c == pair:
                    print(c)
                    continue
                if not dfs(c, node):
                    remove.add((c, node))
                    return False

            cycle.remove(node)
            visited.add(node)
            
            return True
        
        dfs(edges[0][0], -1)
        print(remove)

        for i in range(len(edges) - 1, -1, -1):
            a, b = edges[i]
            if (a, b) in remove or (b, a) in remove:
                return edges[i]

        return remove

        