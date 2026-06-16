from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        courseflow = defaultdict(list)

        for course, preq in prerequisites:
            courseflow[course].append(preq)
        
        visited = set()
        cycle = set()

        result = []
        def dfs(course):
            
            if course in visited:
                return True
    
            if course in cycle:
                return False
            
            cycle.add(course)
            for preq in courseflow[course]:
                if not dfs(preq):
                    return False
            cycle.remove(course)
            visited.add(course)
            result.append(course)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return result
            




        