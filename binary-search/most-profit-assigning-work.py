class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        profits_heap = []
        difficulty_heap = []
        for i in range(len(difficulty)):
            if difficulty[i] <= worker[0]:
                heapq.heappush(profits_heap, (-profit[i], difficulty[i]))
            else:
                heapq.heappush(difficulty_heap, (difficulty[i], profit[i]))

        answer = 0
        for i in range(len(worker)):
            if profits_heap:
                highest_profit, _ = profits_heap[0]
                highest_profit *= -1
                answer += highest_profit
            
            if i < len(worker) - 1 and difficulty_heap:
                curr_diff, curr_prof = heapq.heappop(difficulty_heap)
                while curr_diff <= worker[i + 1]:
                    heapq.heappush(profits_heap, (-curr_prof, curr_diff))
                    if not difficulty_heap:
                        break
                    curr_diff, curr_prof = heapq.heappop(difficulty_heap)
                
                if curr_diff >= worker[i + 1]:
                    heapq.heappush(difficulty_heap, (curr_diff, curr_prof))
        return answer
            
