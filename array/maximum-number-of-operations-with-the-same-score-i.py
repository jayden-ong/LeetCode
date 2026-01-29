class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        prev = None
        answer = 1
        for i in range(2, len(nums) + 1, 2):
            if i == 2:
                prev = nums[i - 1] + nums[i - 2]
            else:
                if nums[i - 1] + nums[i - 2] != prev:
                    return answer
                else:
                    answer += 1
        return answer