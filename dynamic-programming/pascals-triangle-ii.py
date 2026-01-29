class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        prev_row = [1, 1]
        for i in range(2, rowIndex + 1):
            curr_row = [1]
            for j in range(len(prev_row) - 1):
                curr_row.append(prev_row[j] + prev_row[j + 1])
            curr_row.append(1)
            prev_row = curr_row
        return curr_row