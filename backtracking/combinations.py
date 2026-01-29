class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def recursive(curr_index, curr_list, curr_k):
            answer = []
            if curr_k == 0:
                return [curr_list]
            if curr_index > n:
                return []
            
            # Can add current index
            list_copy = curr_list.copy()
            list_copy.append(curr_index)
            answer += recursive(curr_index + 1, list_copy, curr_k - 1)
            # Can move to next
            list_copy = curr_list.copy()
            answer += recursive(curr_index + 1, list_copy, curr_k)
            return answer

        for i in range(1, n + 1):
            answer += recursive(i + 1, [i], k - 1)
        return answer