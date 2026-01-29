class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        length_nums = len(nums)
        answer = 0
        for i in range(length_nums):
            if length_nums % (i + 1) == 0:
                answer += pow(nums[i], 2)
        return answer