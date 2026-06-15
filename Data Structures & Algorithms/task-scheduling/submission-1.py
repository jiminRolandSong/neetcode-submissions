from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        taskcounts = [-count for count in counts.values()]
        heapq.heapify(taskcounts)

        time = 0
        q = deque() #[remaining_count, next_executing_time]

        while q or taskcounts:
            time += 1

            if not taskcounts:
                time = q[0][1]
            else:
                new_count = heapq.heappop(taskcounts) + 1
                if new_count < 0:
                    q.append([new_count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(taskcounts, q.popleft()[0])
        
        return time
        