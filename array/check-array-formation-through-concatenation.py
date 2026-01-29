class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces_dict = {}
        # Each piece starts with a different number
        for piece in pieces:
            pieces_dict[piece[0]] = piece
        
        curr_index = 0
        length_arr = len(arr)
        while curr_index < length_arr:
            if arr[curr_index] not in pieces_dict:
                return False
            else:
                length_piece = len(pieces_dict[arr[curr_index]])
                for i in range(length_piece):
                    if arr[curr_index + i] != pieces_dict[arr[curr_index]][i]:
                        return False
                curr_index += length_piece
        return True