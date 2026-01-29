from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        tuple_board = (tuple(board[0]), tuple(board[1]))
        boards_queue = deque()
        boards_queue.append((tuple_board, 0))
        explored_boards = set()
        explored_boards.add(tuple_board)
        while boards_queue:
            # Check if board is correct
            curr_board, curr_moves = boards_queue.popleft()
            third_board = None
            if curr_board[0] == (1, 2, 3) and curr_board[1] == (4, 5, 0):
                return curr_moves
            
            # Empty tile is in the top left
            if curr_board[0][0] == 0:
                # Swap first and second squares
                first_board = ((curr_board[0][1], 0, curr_board[0][2]), curr_board[1])
                # Swap first and fourth squares
                second_board = ((curr_board[1][0], curr_board[0][1], curr_board[0][2]), (0, curr_board[1][1], curr_board[1][2]))
            # Empty tile is the top
            elif curr_board[0][1] == 0:
                # Swap first and second squares
                first_board = ((0, curr_board[0][0], curr_board[0][2]), curr_board[1])
                # Swap second and third squares
                second_board = ((curr_board[0][0], curr_board[0][2], 0), curr_board[1])
                # Swap second and fourth squares
                third_board = ((curr_board[0][0], curr_board[1][1], curr_board[0][2]), (curr_board[1][0], 0, curr_board[1][2]))
            # Empty tile is the top right
            elif curr_board[0][2] == 0:
                # Swap third and sixth squares
                first_board = ((curr_board[0][0], curr_board[0][1], curr_board[1][2]), (curr_board[1][0], curr_board[1][1], 0))
                # Swap second and third squares
                second_board = ((curr_board[0][0], 0, curr_board[0][1]), curr_board[1])
            # Empty tile is the bottom left
            elif curr_board[1][0] == 0:
                # Swap forth and fifth squares
                first_board = (curr_board[0], (curr_board[1][1], 0, curr_board[1][2]))
                # Swap first and fourth squares
                second_board = ((0, curr_board[0][1], curr_board[0][2]), (curr_board[0][0], curr_board[1][1], curr_board[1][2]))
            # Empty tile is the bottom
            elif curr_board[1][1] == 0:
                # Swap fourth and fifth squares
                first_board = (curr_board[0], (0, curr_board[1][0], curr_board[1][2]))
                # Swap fifth and sixth squares
                second_board = (curr_board[0], (curr_board[1][0], curr_board[1][2], 0))
                # Swap second and fifth squares
                third_board = ((curr_board[0][0], 0, curr_board[0][2]), (curr_board[1][0], curr_board[0][1], curr_board[1][2]))
            # Empty tile is the bottom right
            elif curr_board[1][2] == 0:
                # Swap sixth and fifth squares
                first_board = (curr_board[0], (curr_board[1][0], 0, curr_board[1][1]))
                # Swap forth and sixth squares
                second_board = ((curr_board[0][0], curr_board[0][1], 0), (curr_board[1][0], curr_board[1][1], curr_board[0][2]))
            
            #print(curr_board)
            if first_board not in explored_boards:
                boards_queue.append((first_board, curr_moves + 1))
                explored_boards.add(first_board)
                #print(first_board)
                
            if second_board not in explored_boards:
                boards_queue.append((second_board, curr_moves + 1))
                explored_boards.add(second_board)
                #print(second_board)
                
            if third_board is not None and third_board not in explored_boards:
                boards_queue.append((third_board, curr_moves + 1))
                explored_boards.add(third_board)
                #print(third_board)
            
            #print('----')
        return -1