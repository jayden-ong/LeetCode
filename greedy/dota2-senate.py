from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad_queue = deque()
        dir_queue = deque()
        next_index = len(senate)
        for i in range(len(senate)):
            if senate[i] == "R":
                rad_queue.append(i)
            else:
                dir_queue.append(i)
        
        while rad_queue and dir_queue:
            rad_senator = rad_queue.popleft()
            dir_senator = dir_queue.popleft()
            if rad_senator < dir_senator:
                rad_queue.append(next_index)
            else:
                dir_queue.append(next_index)
            next_index += 1
        
        if dir_queue:
            return "Dire"
        return "Radiant"
