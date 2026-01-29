class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        length_nums = len(nums)
        answer = 0
        for i in range(length_nums - 2):
            for j in range(i + 1, length_nums - 1):
                if nums[i] != nums[j]:
                    for k in range(j + 1, length_nums):
                        if nums[i] != nums[k] and nums[j] != nums[k]:
                            answer += 1
        return answer