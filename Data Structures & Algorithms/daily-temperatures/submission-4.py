class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        temps = []

        for index, temp in enumerate(temperatures):
            while len(temps) > 0 and temps[-1][1] < temp:
                ind, tmp = temps.pop()
                result[ind] = index - ind
            temps.append((index, temp))
        
        return result


        