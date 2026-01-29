from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        reverse_dict = {}
        for starting, ending in edges:
            if ending in reverse_dict:
                reverse_dict[ending].append(starting)
            else:
                reverse_dict[ending] = [starting]
        
        # print(reverse_dict)
        answer = [[]] * n
        
        for i in range(n):
            if i in reverse_dict:
                stack = deque(reverse_dict[i])
                visited = set()
                while stack:
                    curr_node = stack.popleft()
                    if curr_node not in visited and curr_node in reverse_dict:
                        for new_node in reverse_dict[curr_node]:
                            if new_node not in visited:
                                stack.append(new_node)
                    
                    visited.add(curr_node)
                
                curr_answer = list(visited)
                curr_answer.sort()
                answer[i] = curr_answer
        return answer
                    
