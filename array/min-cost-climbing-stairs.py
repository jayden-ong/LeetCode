class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        num_cost = len(cost)
        dpp_dict = {}
        for i in range(2, num_cost + 1):
            if i == 2:
                dpp_dict[i] = min(cost[0], cost[1])
            elif i == 3:
                dpp_dict[i] = min(cost[0] + cost[2], cost[1])
            else:
                dpp_dict[i] = min(dpp_dict[i - 1] + cost[i - 1], dpp_dict[i - 2] + cost[i - 2])
        return dpp_dict[num_cost]