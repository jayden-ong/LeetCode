class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        answer = 0
        # Determines how many elements are in the sliding window
        curr_nums_dict = defaultdict(int)
        curr_nums_dict[nums[0]] += 1
        # Determines the bounds of the list
        curr_min = nums[0] - 2
        curr_max = nums[0] + 2
        # Determines indices of the sliding window
        left = 0
        for right in range(1, len(nums)):
            if nums[right] < curr_min or nums[right] > curr_max:
                while left < right and (nums[right] < curr_min or nums[right] > curr_max):
                    curr_nums_dict[nums[left]] -= 1
                    answer += right - left
                    # Have to update curr_min and curr_max
                    if curr_nums_dict[nums[left]] == 0:
                        if nums[left] - 2 == curr_min:
                            curr_min -= 1
                        
                        if nums[left] + 2 == curr_max:
                            curr_max += 1
                    left += 1
                
                if left == right:
                    curr_min = nums[left] - 2
                    curr_max = nums[left] + 2
            curr_nums_dict[nums[right]] += 1
            curr_min = max(curr_min, nums[right] - 2)
            curr_max = min(curr_max, nums[right] + 2)
        # len(nums) - left is the number of elements in the last subarray
        last_length = len(nums) - left
        answer += ((last_length) * (last_length + 1)) // 2
        return answer
