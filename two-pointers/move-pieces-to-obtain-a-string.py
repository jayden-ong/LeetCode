class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Make sure there is an equal amount of L and R
        start_L, start_R = start.count('L'), start.count('R')
        target_L, target_R = target.count('L'), target.count('R')
        if start_L != target_L or start_R != target_R:
            return False
        
        start_index = 0
        target_index = 0
        num_start = 0
        num_target = 0
        while num_start != start_L + start_R and num_target != target_L + target_R:
            while start[start_index] != 'L' and start[start_index] != 'R':
                start_index += 1
            
            while target[target_index] != 'L' and target[target_index] != 'R':
                target_index += 1
            
            # No way for pieces to jump over each other
            if start[start_index] != target[target_index]:
                return False
            elif start[start_index] == 'L' and start_index < target_index:
                return False
            elif start[start_index] == 'R' and start_index > target_index:
                return False
            
            num_start += 1
            num_target += 1
            start_index += 1
            target_index += 1

        return True