class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if minutes == len(customers):
            return sum(customers)
        
        curr = 0
        for i in range(len(customers)):
            if grumpy[i] == 0 or i < minutes:
                curr += customers[i]
        
        answer = curr
        for i in range(minutes, len(customers)):
            print(answer)
            if grumpy[i - minutes]:
                curr -= customers[i - minutes]
            
            if grumpy[i]:
                curr += customers[i]
            answer = max(curr, answer)
        return answer
