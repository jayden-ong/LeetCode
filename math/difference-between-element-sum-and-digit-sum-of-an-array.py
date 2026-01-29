class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            string_num = str(num)
            for char in string_num:
                digit_sum += int(char)
        return abs(element_sum - digit_sum)