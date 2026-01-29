class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Answer must be between 0 and length of nums
        length_nums = len(nums)
        nums.sort()
        curr_pos = 0
        num_elements = length_nums
        for i in range(length_nums + 1):
            while curr_pos < length_nums and nums[curr_pos] < i:
                curr_pos += 1
                num_elements -= 1
            
            if curr_pos >= length_nums or num_elements < i:
                return -1
            
            if num_elements == i:
                return i
        return -1