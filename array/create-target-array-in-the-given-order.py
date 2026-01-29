class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        length_nums = len(nums)
        answer = []
        for i in range(length_nums):
            answer.insert(index[i], nums[i])
        return answer