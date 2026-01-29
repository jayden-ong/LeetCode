class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes_dict = {}
        answer = 0
        for i in range(lowLimit, highLimit + 1):
            string_num = str(i)
            box = 0
            for char in string_num:
                box += int(char)
            
            if box in boxes_dict:
                boxes_dict[box] += 1
            else:
                boxes_dict[box] = 1

            answer = max(answer, boxes_dict[box])
        return answer