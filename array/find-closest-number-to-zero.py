class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        answer = None
        for num in nums:
            if answer is None or abs(num) < abs(answer) or (abs(num) == abs(answer) and num > answer):
                answer = num
        return answer