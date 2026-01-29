class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # First have to determine the dominant element
        nums_dict = defaultdict(int)
        curr_dominant = None
        freq = 0
        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] > freq:
                curr_dominant = num
                freq = nums_dict[num]
        
        dominant_freq = 0
        for i in range(len(nums) - 1):
            if nums[i] == curr_dominant:
                dominant_freq += 1
            
            first_array_length = i + 1
            last_array_length = len(nums) - i - 1
            if dominant_freq / first_array_length > 0.5 and (freq - dominant_freq) / last_array_length > 0.5:
                return i
        return -1