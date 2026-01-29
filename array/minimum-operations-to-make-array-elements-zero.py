class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # Use math.floor(math.log(query)) + 1 to get number of operations
        def find_num_operations(num):
            answer = 0
            curr_base = 1
            while curr_base <= num:
                # Need to figure out how many numbers have this base
                amount = min(curr_base * 4, num + 1) - curr_base
                answer += (math.floor(math.log(curr_base, 4)) + 1) * amount
                curr_base *= 4
            return answer
        
        answer = 0
        for left, right in queries:
            query_answer = find_num_operations(right) - find_num_operations(left - 1)
            answer += query_answer // 2
            if query_answer % 2 == 1:
                answer += 1
        return answer