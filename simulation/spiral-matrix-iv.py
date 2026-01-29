# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n
        # Initialize matrix
        answer = []
        row = [-1] * n
        for i in range(m):
            answer.append(row.copy())
        
        curr_row, curr_col = 0, 0
        curr = head
        direction_index = 0
        while curr is not None:
            answer[curr_row][curr_col] = curr.val
            curr = curr.next
            temp_row, temp_col = curr_row + directions[direction_index][0], curr_col + directions[direction_index][1]
            if is_valid(temp_row, temp_col) and answer[temp_row][temp_col] == -1:
                curr_row, curr_col = temp_row, temp_col
                continue
            else:
                direction_index = (direction_index + 1) % 4
                curr_row, curr_col = curr_row + directions[direction_index][0], curr_col + directions[direction_index][1]
        return answer

