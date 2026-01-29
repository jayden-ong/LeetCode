class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(num):
            string_num = str(num)
            answer = 0
            for char in string_num:
                answer += int(char)
            return answer

        groups_dict = {}
        max_digits = 0
        for i in range(1, n + 1):
            sum_of_digits = sum_digits(i)
            if sum_of_digits in groups_dict:
                groups_dict[sum_of_digits] += 1
            else:
                groups_dict[sum_of_digits] = 1
            max_digits = max(groups_dict[sum_of_digits], max_digits)
        
        curr_max = 0
        answer = 1
        for key in groups_dict:
            if groups_dict[key] > curr_max:
                curr_max = groups_dict[key]
                answer = 1
            elif groups_dict[key] == curr_max:
                answer += 1 
        return answer