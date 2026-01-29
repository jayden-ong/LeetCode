class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []
        i = 0
        while i < len(nums):
            answer.append(nums[i + 1])
            answer.append(nums[i])
            i += 2
        return answer