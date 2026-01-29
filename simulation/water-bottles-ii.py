class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def exchange(num_empty, exchange_rate):
            num_full = 0
            while num_empty >= exchange_rate:
                num_empty -= exchange_rate
                num_full += 1
                exchange_rate += 1
            return num_full, num_empty, exchange_rate
        
        answer = numBottles
        num_empty = numBottles
        while num_empty >= numExchange:
            # Exchange empty bottles for full bottles
            num_full, num_empty, numExchange = exchange(num_empty, numExchange)
            # Drink full bottles and convert to empty
            answer += num_full
            num_empty += num_full
        return answer