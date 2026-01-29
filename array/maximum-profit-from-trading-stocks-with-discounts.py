class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        hierarchy_dict = defaultdict(set)
        for boss, employee in hierarchy:
            hierarchy_dict[boss - 1].add(employee - 1)
        
        def determine_max_profit(curr_node):
            cost, d_cost = present[curr_node], present[curr_node] // 2
            max_profit, d_max_profit = [0] * (budget + 1), [0] * (budget + 1)
            sub_profit, d_sub_profit = [0] * (budget + 1), [0] * (budget + 1)

            curr_cost = cost
            for child in hierarchy_dict[curr_node]:
                child_max_profit, child_d_max_profit, child_cost = determine_max_profit(child)
                curr_cost += child_cost
                for i in range(budget, -1, -1):
                    for sub_p in range(min(child_cost, i) + 1):
                        if i - sub_p >= 0:
                            sub_profit[i] = max(sub_profit[i], sub_profit[i - sub_p] + child_max_profit[sub_p])
                            d_sub_profit[i] = max(d_sub_profit[i], d_sub_profit[i - sub_p] + child_d_max_profit[sub_p])
                
            for i in range(budget + 1):
                max_profit[i], d_max_profit[i] = sub_profit[i], sub_profit[i]
                if i >= d_cost:
                    d_max_profit[i] = max(sub_profit[i], d_sub_profit[i - d_cost] + future[curr_node] - d_cost)
                if i >= cost:
                    max_profit[i] = max(sub_profit[i], d_sub_profit[i - cost] + future[curr_node] - cost)
            return max_profit, d_max_profit, curr_cost

        return determine_max_profit(0)[0][budget]

