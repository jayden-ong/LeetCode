class Solution:
    def bestClosingTime(self, customers: str) -> int:
        num_customers = 0
        for customer in customers:
            if customer == "Y":
                num_customers += 1
        
        idle_time = 0
        optimal, answer = 0, num_customers
        # Every customer that comes on or after the closing hour counts as penalty
        for i, customer in enumerate(customers):            
            if customer == "Y":
                num_customers -= 1
            else:
                idle_time += 1
            
            if num_customers + idle_time < answer:
                optimal, answer = i + 1, num_customers + idle_time

        return optimal