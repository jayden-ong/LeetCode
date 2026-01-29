class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        num_rows = len(board)
        num_cols = len(board[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def is_valid(i, j):
            return 0 <= i < num_rows and 0 <= j < num_cols
        answer = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == "X" and (i, j) not in visited:
                    visited.add((i, j))
                    curr = [(i, j)]
                    while curr:
                        curr_i, curr_j = curr.pop()
                        for direction in directions:
                            new_i, new_j = direction[0] + curr_i, direction[1] + curr_j
                            if is_valid(new_i, new_j) and board[new_i][new_j] == "X" and (new_i, new_j) not in visited:
                                curr.append((new_i, new_j))
                                visited.add((new_i, new_j))
                                break
                    answer += 1
        return answer