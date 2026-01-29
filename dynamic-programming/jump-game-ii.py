class Solution:
    def jump(self, nums: List[int]) -> int:
        num_spaces = len(nums)
        if num_spaces == 1:
            return 0
        
        curr_pos = 0
        num_jumps = 0
        while curr_pos != num_spaces - 1:
            maximum_jump = nums[curr_pos]
            if curr_pos + maximum_jump >= num_spaces - 1:
                return num_jumps + 1
            
            most_potential = nums[curr_pos + 1] + 1
            most_potential_index = curr_pos + 1
            for i in range(curr_pos + 2, curr_pos + maximum_jump + 1):
                if nums[i] > 0:
                    potential = i - curr_pos + nums[i]
                    if potential > most_potential:
                        most_potential = potential
                        most_potential_index = i
            curr_pos = most_potential_index
            num_jumps += 1
        return num_jumps