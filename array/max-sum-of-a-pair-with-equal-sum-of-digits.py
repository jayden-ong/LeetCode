class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            str_num = str(num)
            answer = 0
            for digit in str_num:
                answer += int(digit)
            return answer
        
        digit_sum_dict = {}
        answer = -1
        for num in nums:
            digit_sum = get_digit_sum(num)
            if digit_sum not in digit_sum_dict:
                digit_sum_dict[digit_sum] = [None, num]
            else:
                if num > digit_sum_dict[digit_sum][1]:
                    digit_sum_dict[digit_sum] = [digit_sum_dict[digit_sum][1], num]
                elif digit_sum_dict[digit_sum][0] is None or num > digit_sum_dict[digit_sum][0]:
                    digit_sum_dict[digit_sum][0] = num
            
            if digit_sum_dict[digit_sum][0] is not None:
                answer = max(answer, digit_sum_dict[digit_sum][0] + digit_sum_dict[digit_sum][1])
        return answer