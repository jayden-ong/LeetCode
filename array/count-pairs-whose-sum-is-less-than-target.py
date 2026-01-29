class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = 0
        num_nums = len(nums)
        for i in range(num_nums - 1):
            for j in range(i + 1, num_nums):
                if nums[i] + nums[j] < target:
                    answer += 1
                else:
                    break
        return answer