class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num_nums = len(nums)
        answer = [0] * num_nums * 2
        for i in range(num_nums):
            answer[i] = nums[i]
            answer[i + num_nums] = nums[i]
        return answer