class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        num_nums = len(nums)
        answer = 0
        for i in range(num_nums - 1):
            for j in range(i + 1, num_nums):
                if abs(nums[i] - nums[j]) == k:
                    answer += 1
        return answer