from collections import deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        '''
        # Adding another path can only improve the previous smallest distances
        # If previous length is 1, the distance will always be 1
        best_path = n - 1
        answer = []
        bridges_dict = defaultdict(list)
        for start, end in queries:
            found_better = False
            bridges_dict[start].append(end)
            paths_queue = deque()
            paths_queue.append((0, 0))
            while paths_queue:
                curr_node, curr_moves = paths_queue.popleft()
                if curr_node == n - 1:
                    answer.append(curr_moves)
                    found_better = True
                    break
                
                if curr_moves >= best_path - 1:
                    continue
                else:
                    paths_queue.append((curr_node + 1, curr_moves + 1))
                    for end in bridges_dict[curr_node]:
                        paths_queue.append((end, curr_moves + 1))
            
            if found_better:
                best_path = answer[-1]
            else:
                answer.append(best_path)
        return answer
        '''
        dp = []
        answer = []
        # Will map each city to all the cities before it that are directly connected to it
        bridges_dict = defaultdict(list)
        for i in range(n):
            dp.append(i)
            if i > 0:
                bridges_dict[i].append(i - 1)
        
        for start, end in queries:
            bridges_dict[end].append(start)
            # Only care about cities after end
            for i in range(end, n):
                for origin in bridges_dict[i]:
                    dp[i] = min(dp[origin] + 1, dp[i])
            answer.append(dp[-1])
        return answer