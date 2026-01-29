class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        curr_length = 1
        answer = 1
        prev_length = None
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] < nums[i + 1]:
                curr_length += 1
            else:
                # The current subarray is a candidate
                answer = max(answer, curr_length // 2)
                if prev_length is not None:
                    answer = max(answer, (min(curr_length, prev_length)))
                prev_length = curr_length
                curr_length = 1
        
        return answer