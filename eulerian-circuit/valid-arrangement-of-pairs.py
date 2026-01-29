class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj_dict = defaultdict(deque)
        start_dict, end_dict = defaultdict(int), defaultdict(int)
        for start, end in pairs:
            adj_dict[start].append(end)
            start_dict[start] += 1
            end_dict[end] += 1
        
        answer = []
        # There will be at most one number that has more starts than ends
        must_start = None
        for num in start_dict:
            if start_dict[num] >= end_dict[num] + 1:
                must_start = num
                break
        
        if must_start is None:
            must_start = pairs[0][0]
        
        def find_path(curr_start):
            while adj_dict[curr_start]:
                next_num = adj_dict[curr_start].popleft()
                find_path(next_num)
            answer.append(curr_start)
        
        find_path(must_start)
        print(answer)
        answer = answer[::-1]
        final_answer = []
        for i in range(len(answer) - 1):
            final_answer.append((answer[i], answer[i + 1]))
        return final_answer