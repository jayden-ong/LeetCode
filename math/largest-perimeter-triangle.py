from collections import deque
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sum of two side lengths must be greater than last side length
        max_perim = 0
        num_lengths = len(nums)
        nums.sort()
        window_list = deque()
        window_list.append(nums[-1])
        window_list.append(nums[-2])
        window_list.append(nums[-3])
        if window_list[0] + window_list[1] > window_list[2] and window_list[1] + window_list[2] > window_list[0] and window_list[0] + window_list[2] > window_list[1]:
            return window_list[0] + window_list[1] + window_list[2]
        
        for i in range(num_lengths - 4, -1, -1):
            window_list.popleft()
            window_list.append(nums[i])
            if window_list[0] + window_list[1] > window_list[2] and window_list[1] + window_list[2] > window_list[0] and window_list[0] + window_list[2] > window_list[1]:
                return window_list[0] + window_list[1] + window_list[2]
            
        return 0