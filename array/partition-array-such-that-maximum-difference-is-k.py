class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr_min = nums[0]
        answer = 1
        for i in range(1, len(nums)):
            if nums[i] - curr_min > k:
                answer += 1
                curr_min = nums[i]
        return answer