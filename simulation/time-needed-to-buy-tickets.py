class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        curr_time = 0
        ticket_wait = tickets[k]
        ticket_wait_less = ticket_wait - 1
        for i in range(len(tickets)):
            if i < k:
                curr_time += min(tickets[i], ticket_wait)
            elif i == k:
                curr_time += ticket_wait
            else:
                curr_time += min(tickets[i], ticket_wait_less)
        return curr_time