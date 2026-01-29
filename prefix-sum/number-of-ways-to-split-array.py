class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        curr_sum = 0
        remaining = sum(nums)
        answer = 0
        for i in range(len(nums) - 1):
            num = nums[i]
            curr_sum += num
            remaining -= num
            if curr_sum >= remaining:
                answer += 1
        return answer