class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        answer = 0
        for i in range(len(nums) - 1):
            if abs(right_sum - left_sum) % 2 == 0:
                answer += 1
        return answer