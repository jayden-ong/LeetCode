class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        answer = 0
        length_cost = len(cost)
        for i in range(length_cost - 1, -1, -3):
            answer += cost[i]
            if i - 1 >= 0:
                answer += cost[i - 1]
        return answer