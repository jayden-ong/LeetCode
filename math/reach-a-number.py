class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        curr_index = 1
        curr_sum = 0
        while curr_sum < target:
            curr_sum += curr_index
            curr_index += 1
        
        if curr_sum == target:
            return curr_index - 1
        
        if (curr_sum - target) % 2 == 0:
            return curr_index - 1
        else:
            if (curr_sum - target + curr_index) % 2 == 0:
                return curr_index
            return curr_index + 1