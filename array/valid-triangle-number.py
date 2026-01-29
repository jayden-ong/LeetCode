class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for i in range(len(nums) - 1, 0, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] <= nums[i]:
                    left += 1
                else:
                    answer += right - left
                    right -= 1
        return answer