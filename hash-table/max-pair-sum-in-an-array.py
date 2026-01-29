class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def get_largest_digit(num: int):
            string_num = str(num)
            answer = 0
            for i in range(len(string_num)):
                answer = max(answer, int(string_num[i]))
            return answer

        largest_digit = []
        for num in nums:
            largest_digit.append(get_largest_digit(num))
        
        num_nums = len(nums)
        answer = -1
        for i in range(num_nums - 1):
            for j in range(i + 1, num_nums):
                if largest_digit[i] == largest_digit[j]:
                    answer = max(answer, nums[i] + nums[j])
        return answer