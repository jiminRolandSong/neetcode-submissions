from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.emos = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.emos:
            self.emos[key] = []

        self.emos[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        emotion = ""
        values = self.emos.get(key, [])
        print(values)

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            time = values[mid][1]

            if values[mid][1] <= timestamp:
                emotion = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return emotion

        
