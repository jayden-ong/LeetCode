class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            num = abs(num)
            # Each num is assigned an int
            if nums[num - 1] < 0:
                answer.append(num)
            nums[num - 1] *= -1
        return answer
            