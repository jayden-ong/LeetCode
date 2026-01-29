class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        num_beams_prev_row = 0
        answer = 0
        for i in range(len(bank)):
            curr_beams = 0
            for j in range(len(bank[0])):
                if bank[i][j] == "1":
                    curr_beams += 1
            
            if curr_beams > 0:
                answer += num_beams_prev_row * curr_beams
                num_beams_prev_row = curr_beams
        return answer