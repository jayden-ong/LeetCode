class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        edges_dict = defaultdict(list)
        left = right = 0
        for start, end, cost in edges:
            if online[start] and online[end]:
                edges_dict[start].append((end, cost))
                right = max(right, cost)
        
        def solve(score):
            distances = [float('inf')] * len(online)
            priority_queue = [(0, 0)]
            distances[0] = 0

            while priority_queue:
                distance, node = heapq.heappop(priority_queue)
                if distance > k:
                    continue
                if node == len(online) - 1:
                    return True
                if distance > distances[node]:
                    continue

                for end, cost in edges_dict[node]:
                    if cost < score:
                        continue
                    if distances[end] > distances[node] + cost:
                        distances[end] = distances[node] + cost
                        heapq.heappush(priority_queue, (distances[end], end))
            return False
        
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if solve(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer
