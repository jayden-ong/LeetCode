class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(rowSum)):
            curr_row = []
            for j in range(len(colSum)):
                new_entry = min(rowSum[i], colSum[j])
                curr_row.append(new_entry)
                rowSum[i] -= new_entry
                colSum[j] -= new_entry
            answer.append(curr_row)
        return answer