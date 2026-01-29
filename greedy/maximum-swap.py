from collections import deque
class Solution:
    def maximumSwap(self, num: int) -> int:
        # Want to swap the largest, THEN latest digit
        # Create list that stores largest digit after
        string_num = str(num)
        curr_largest = None
        largest_after = deque()
        for i in range(len(string_num) - 1, -1, -1):
            if curr_largest is None or int(string_num[i]) > curr_largest:
                curr_largest = int(string_num[i])
            
            largest_after.appendleft(curr_largest)
        
        answer = [-1] * len(string_num)
        done_swapping = False
        for i in range(len(string_num)):
            if (largest_after[i] == int(string_num[i]) or done_swapping) and answer[i] == -1:
                answer[i] = string_num[i]
            elif not done_swapping:
                for j in range(len(string_num) - 1, -1, -1):
                    if string_num[j] == str(largest_after[i]):
                        answer[i] = str(largest_after[i])
                        answer[j] = string_num[i]
                        break
                done_swapping = True
        return int(''.join(answer))
            
        