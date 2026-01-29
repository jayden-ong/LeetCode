class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        edges_dict = defaultdict(list)  
        in_degree = [0] * len(colors)  
        for start, end in edges:
            edges_dict[start].append(end)
            in_degree[end] += 1
        
        curr_queue = deque()
        for i in range(len(colors)):
            if in_degree[i] == 0:
                curr_queue.append(i)
        def perform_topo_sort(curr_vertex, visited, answer):
            visited[curr_vertex] = True
            for end in edges_dict[curr_vertex]:
                if not visited[end]:
                    perform_topo_sort(end, visited, answer)
            answer.append(curr_vertex)
        
        def detect_cycle(queue):
            num_visited = 0
            while queue:
                curr_node = queue.popleft()
                num_visited += 1
                for new_node in edges_dict[curr_node]:
                    in_degree[new_node] -= 1
                    if in_degree[new_node] == 0:
                        queue.append(new_node)
            return len(colors) != num_visited

        if detect_cycle(curr_queue):
            return -1
        
        topo_sort = []
        visited = [False] * len(colors)
        dp = {}
        for i in range(len(colors)):
            if not visited[i]:
                perform_topo_sort(i, visited, topo_sort)
            dp[i] = defaultdict(int)
        
        answer = 1
        for node in topo_sort:
            dp[node][colors[node]] += 1
            for end in edges_dict[node]:
                for color in dp[end]:
                    if color == colors[node]:
                        dp[node][color] = max(1 + dp[end][color], dp[node][color])
                    else:
                        dp[node][color] = max(dp[end][color], dp[node][color])
                    answer = max(answer, dp[node][color])
        return answer