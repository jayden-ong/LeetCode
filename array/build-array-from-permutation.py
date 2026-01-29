class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        num_nums = len(nums)
        answer = [0] * num_nums
        for i in range(num_nums):
            answer[i] = nums[nums[i]]
        return answer