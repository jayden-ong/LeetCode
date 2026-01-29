class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # keep track of the amount of balls to the left of current index and to the right
        curr_moves = 0
        curr_right = 0
        for i in range(len(boxes)):
            curr_moves += int(boxes[i]) * i
            if boxes[i] == '1':
                curr_right += 1
        
        answer = []
        curr_left = 0
        for i in range(len(boxes)):
            answer.append(curr_moves)
            if boxes[i] == '1':
                curr_left += 1
                curr_right -= 1
            
            # Gets farther from the ones to the left
            curr_moves += curr_left
            # Gets closer to the ones on the right
            curr_moves -= curr_right
        return answer