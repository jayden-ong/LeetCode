class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = pow(10, 9) + 7
        num_seats = 0
        seat_locations = []
        for i, item in enumerate(corridor):
            if item == "S":
                num_seats += 1
                seat_locations.append(i)
        
        if num_seats % 2 == 1 or 0 <= num_seats <= 1:
            return 0
        elif num_seats == 2:
            return 1
        
        answer = 1
        for i in range(1, num_seats - 1, 2):
            # The amount of plants between pairs of chairs determines how many different ways we can divide the corridor
            answer = (answer * (seat_locations[i + 1] - seat_locations[i])) % MOD

        return answer