class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # ord('a') = 97 and ord('z') = 122
        answer = []
        moves = [0] * len(s)
        for char in s:
            answer.append(char)
        
        for start, end, direction in shifts:
            if direction == 0:
                moves[start] -= 1
                if end < len(s) - 1:
                    moves[end + 1] += 1
            else:
                moves[start] += 1
                if end < len(s) - 1:
                    moves[end + 1] -= 1
        
        curr = 0
        for i in range(len(moves)):
            curr += moves[i]
            char_num = ord(answer[i]) + curr
            char_num = (char_num - 97) % 26
            answer[i] = chr(char_num + 97)
        return ''.join(answer)