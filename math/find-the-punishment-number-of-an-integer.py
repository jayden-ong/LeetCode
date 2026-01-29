class Solution:
    def punishmentNumber(self, n: int) -> int:
        def validate_partition(target_num, target_num_sq, curr_sum, curr_num, curr_digit_pos):
            # Stop early
            if curr_sum > target_num:
                return False

            if curr_digit_pos == len(str(target_num_sq)):
                if curr_sum + int(curr_num) == target_num:
                    return True
                return False
            
            # two options
            # add the next digit to the current num
            if validate_partition(target_num, target_num_sq, curr_sum, curr_num + str(target_num_sq)[curr_digit_pos], curr_digit_pos + 1):
                return True
            
            # end curr_num and start anew
            if curr_num != "" and validate_partition(target_num, target_num_sq, curr_sum + int(curr_num), str(target_num_sq)[curr_digit_pos], curr_digit_pos + 1):
                return True
            return False
        
        answer = 0
        for i in range(1, n + 1):
            if validate_partition(i, i * i, 0, "", 0):
                answer += i * i
        return answer