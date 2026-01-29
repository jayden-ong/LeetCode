class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_nums = len(nums)
        answer = 0
        for i in range(num_nums - 2):
            for j in range(i + 1, num_nums - 1):
                if nums[j] - nums[i] == diff:
                    for k in range(j + 1, num_nums):
                        if nums[k] - nums[j] == diff:
                            answer += 1
        return answer