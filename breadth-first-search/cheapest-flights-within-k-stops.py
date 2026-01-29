from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs_array = [float('inf')] * n
        costs_array[src] = 0
        for i in range(k + 1):
            temp_costs = costs_array.copy()
            for curr_src, curr_dest, curr_price in flights:
                if costs_array[curr_src] != float('inf'):
                    temp_costs[curr_dest] = min(costs_array[curr_src] + curr_price, temp_costs[curr_dest])
            costs_array = temp_costs
        if costs_array[dst] == float('inf'):
            return -1
        return costs_array[dst]
