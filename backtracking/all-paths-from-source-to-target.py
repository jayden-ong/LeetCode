from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = deque()
        queue.append([0, [0]])
        answer = []
        while queue:
            curr_node, curr_path = queue.popleft()
            if curr_node == len(graph) - 1:
                answer.append(curr_path)
            else:
                for new_node in graph[curr_node]:
                    queue.append([new_node, curr_path + [new_node]])
        return answer
                    