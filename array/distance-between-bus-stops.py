class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        num_distances = len(distance)
        curr_location = start
        # Start by increasing
        curr_cost = 0
        while curr_location != destination:
            curr_cost += distance[curr_location]
            if curr_location == num_distances - 1:
                curr_location = 0
            else:
                curr_location += 1
        
        second_cost = 0
        curr_location = start
        while curr_location != destination:
            if curr_location == 0:
                curr_location = num_distances - 1
            else:
                curr_location -= 1
            second_cost += distance[curr_location]
        return min(curr_cost, second_cost)