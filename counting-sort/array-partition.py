class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Want to pair the min with min
        nums.sort()
        num_nums = len(nums)
        curr_sum = 0
        for i in range(0, num_nums, 2):
            curr_sum += nums[i]
        return curr_sum