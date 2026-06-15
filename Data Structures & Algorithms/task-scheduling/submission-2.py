from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        count_heap = [-cnt for cnt in count.values()]
        heapq.heapify(count_heap)

        time = 0
        q = deque()

        while q or count_heap:
            time += 1

            if not count_heap:
                time = q[0][1]
            else:
                new_count = heapq.heappop(count_heap) + 1
                if new_count < 0:
                    q.append([new_count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(count_heap, q.popleft()[0])
        
        return time
        