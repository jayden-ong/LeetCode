class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = 0
        answer = 0
        for num in nums:
            if pos != 0 and pos + num == 0:
                answer += 1
            pos += num
        return answer