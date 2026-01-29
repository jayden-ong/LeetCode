class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def is_increasing(arr):
            for i in range(1, len(arr)):
                if arr[i - 1] >= arr[i]:
                    return False
            return True
        
        answer = 0
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                sub_array = nums[j:j + i]
                new_array = nums[:j] + nums[j + i + 1:]
                if is_increasing(new_array):
                    answer += 1
        return answer
