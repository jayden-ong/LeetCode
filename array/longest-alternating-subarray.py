class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        answer = 0
        num_nums = len(nums)
        i = 0
        while i < num_nums - 1 and nums[i] + 1 != nums[i + 1]:
            i += 1
        
        if i >= num_nums - 1:
            return -1
        
        curr_sequence = [nums[i], nums[i + 1]]
        curr_streak = 2
        curr_index = 0

        j = i + 2
        while j < num_nums:
            if curr_sequence[curr_index] == nums[j]:
                curr_streak += 1
                curr_index = 1 - curr_index
                j += 1
            else:
                answer = max(curr_streak, answer)
                j -= 1
                while j < num_nums - 1 and nums[j] + 1 != nums[j + 1]:
                    j += 1

                if j >= num_nums - 1:
                    return max(curr_streak, answer)

                curr_sequence = [nums[j], nums[j + 1]]
                curr_index = 0
                curr_streak = 2
                j += 2
            
        return max(curr_streak, answer)