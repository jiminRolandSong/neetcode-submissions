class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleets = []

        for pos, spe in sorted(zip(position, speed), reverse=True):
            check = (target - pos) / spe

            if len(fleets) > 0 and fleets[-1] < check:             
                fleets.append(check)
            elif len(fleets) == 0:
                fleets.append(check)
        
        return len(fleets)
                

        