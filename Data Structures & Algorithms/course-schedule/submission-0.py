from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pres = defaultdict(list)

        for course, prereq in prerequisites:
            pres[course].append(prereq)
        
        visiting = set()

        def dfs(course):
            if course not in pres:
                return True
            
            if course in visiting:
                return False
            
            visiting.add(course)
            for preq in pres[course]:
                if not dfs(preq):
                    return False
            visiting.remove(course)
            
            return True
        
        for course in pres:
            if not dfs(course):
                return False
        
        return True


        