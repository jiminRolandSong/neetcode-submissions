class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        left = 0
        right = len(people) - 1
        count = 0

        while left <= right:
            remaining = limit - people[right]
            count += 1
            right -= 1

            if people[left] <= remaining and left <= right:
                left += 1
        return count
        