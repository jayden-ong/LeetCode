class Solution:
    def countPoints(self, rings: str) -> int:
        answer_dict = {}
        length_rings = len(rings)
        for i in range(0, length_rings, 2):
            ring_color = rings[i]
            rod_number = rings[i + 1]
            if rod_number in answer_dict:
                if ring_color not in answer_dict[rod_number]:
                    answer_dict[rod_number].append(ring_color)
            else:
                answer_dict[rod_number] = [ring_color]
        
        answer = 0
        for rod in answer_dict:
            if len(answer_dict[rod]) == 3:
                answer += 1
        return answer