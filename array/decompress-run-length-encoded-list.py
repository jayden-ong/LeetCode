class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums), 2):
            answer += [nums[i + 1]] * nums[i]
        return answer