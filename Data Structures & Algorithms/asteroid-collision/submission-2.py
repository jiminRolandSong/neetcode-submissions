class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        survivors = []

        for a in asteroids:
            survived = True
            while len(survivors) > 0 and a < 0 and survivors[-1] > 0 and survived:
                front = survivors[-1]
                if abs(front) < abs(a):
                    survivors.pop()
                elif abs(front) > abs(a):
                    survived = False
                else:
                    survivors.pop()
                    survived = False
            
            if survived:
                survivors.append(a)
            
        
        return survivors

        
        