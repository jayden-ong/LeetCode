class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        length_nums = len(nums)
        answer = 0
        for i in range(length_nums - 3):
            for j in range(i + 1, length_nums - 2):
                for k in range(j + 1, length_nums - 1):
                    for w in range(k + 1, length_nums):
                        if nums[i] + nums[j] + nums[k] == nums[w]:
                            answer += 1
        return answer