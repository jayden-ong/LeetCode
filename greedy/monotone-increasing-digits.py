class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        string_n = str(n)
        num_digits = len(string_n)
        problem_location = -1
        for i in range(num_digits - 1):
            if int(string_n[i + 1]) < int(string_n[i]):
                problem_location = i
                break
        if problem_location == -1:
            return n
        
        curr_result = []
        solution_found = -1
        for i in range(problem_location, 0, -1):
            if int(string_n[i]) > int(string_n[i - 1]):
                solution_found = i
                break

        # Need to decrease the first digit
        if solution_found == -1:
            num_digits_to_add = num_digits
            # Need to append 9 and there will be 1 less digit
            if string_n[0] == "1":
                curr_result.append("9")
                num_digits_to_add -= 2
            else:
                first_digit = int(string_n[0]) - 1
                curr_result.append(str(first_digit))
                num_digits_to_add -= 1
        else:
            for i in range(solution_found):
                curr_result.append(string_n[i])
            curr_result.append(str(int(string_n[solution_found]) - 1))
            num_digits_to_add = num_digits - solution_found - 1
        curr_result = curr_result + (["9"] * num_digits_to_add)

        return int(''.join(curr_result))