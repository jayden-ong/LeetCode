class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = 0
        answer = []
        for num in nums:
            curr_sum += num
            answer.append(curr_sum)
        return answer