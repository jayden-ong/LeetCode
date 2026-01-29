class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        answer = []
        curr_index = 0
        for i in range(m):
            curr_row = []
            for j in range(n):
                curr_row.append(original[curr_index])
                curr_index += 1
            answer.append(curr_row)
        return answer