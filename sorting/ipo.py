class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        '''
        Scan the list of capitals and choose to invest in the one with the most profit
        that has a capital requirement lower than the capital you currently have. 
        '''
        curr_capital = w
        # Want to sort by profits
        viable_profits_heap = []
        # Want to sort by smallest capital
        unviable_capital_heap = []
        for i in range(len(profits)):
            if capital[i] <= curr_capital:
                heapq.heappush(viable_profits_heap, (-profits[i], capital[i]))
            else:
                heapq.heappush(unviable_capital_heap, (capital[i], profits[i]))

        for i in range(min(len(capital), k)):
            # If there are no more viable profits, nothing else can be added
            if not viable_profits_heap:
                return curr_capital
            
            curr_profit, _ = heapq.heappop(viable_profits_heap)
            curr_profit *= -1
            curr_capital += curr_profit

            # With our capital increased, we should have access to more projects
            while unviable_capital_heap:
                next_capital, next_profit = heapq.heappop(unviable_capital_heap)
                if next_capital <= curr_capital:
                    heapq.heappush(viable_profits_heap, (-next_profit, next_capital))
                else:
                    heapq.heappush(unviable_capital_heap, (next_capital, next_profit))
                    break
            
        return curr_capital