class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        heapq.heapify(players)
        heapq.heapify(trainers)
        answer = 0
        while players and trainers:
            while trainers and players[0] > trainers[0]:
                heapq.heappop(trainers)
            
            if trainers:
                answer += 1
                heapq.heappop(trainers)
            heapq.heappop(players)
        return answer