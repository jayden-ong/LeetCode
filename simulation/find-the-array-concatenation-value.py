class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        num_nums = len(nums)
        left = 0
        right = num_nums - 1
        answer = 0
        while left <= right:
            if left == right:
                answer += nums[left]
            else:
                answer += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        return answer