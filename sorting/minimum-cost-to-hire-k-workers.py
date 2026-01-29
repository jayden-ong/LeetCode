from operator import itemgetter
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # How much should you pay for one unit of work?
        num_quality = len(quality)
        quality_wage_pairs = []
        for i in range(num_quality):
            quality_wage_pairs.append((quality[i], wage[i],wage[i] / quality[i]))
        
        answer = float('inf')
        # Want to sort by cost per unit of work
        quality_wage_pairs.sort(key=itemgetter(2))
        heap = []
        total_quality = 0
        for i in range(num_quality):
            if i < k:
                heapq.heappush(heap, -quality_wage_pairs[i][0])
                total_quality += quality_wage_pairs[i][0]
                if i == k - 1:
                    answer = min(answer, total_quality * quality_wage_pairs[i][2])
            else:
                total_quality += quality_wage_pairs[i][0]
                heapq.heappush(heap, -quality_wage_pairs[i][0])
                total_quality += heapq.heappop(heap)
                answer = min(answer, total_quality * quality_wage_pairs[i][2])
        return answer