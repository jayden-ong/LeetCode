class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        longest_increasing_subsequence = [1] * len(nums)
        longest_decreasing_subsequence = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    longest_increasing_subsequence[i] = max(longest_increasing_subsequence[i], longest_increasing_subsequence[j] + 1)
                
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    longest_decreasing_subsequence[i] = max(longest_decreasing_subsequence[i], longest_decreasing_subsequence[j] + 1)
        
        answer = 0
        for i in range(1, len(nums) - 1):
            if longest_increasing_subsequence[i] > 1 and longest_decreasing_subsequence[i] > 1:
                answer = max(answer, longest_increasing_subsequence[i] + longest_decreasing_subsequence[i] - 1)
        return len(nums) - answer

        