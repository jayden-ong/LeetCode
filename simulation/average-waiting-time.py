class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = -1
        answer = 0
        for start, wait in customers:
            if curr_time < start:
                curr_time = start
            
            curr_time += wait
            answer += curr_time - start
        return answer / len(customers)