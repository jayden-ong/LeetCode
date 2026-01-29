class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) % 2 == 0:
            median = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) // 2
        else:
            median = nums[len(nums) // 2]
        # Try getting average rounded down
        answer = 0
        for num in nums:
            answer += abs(num - median)
        return answer