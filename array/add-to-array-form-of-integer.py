class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        string_k = str(k)
        length_k = len(string_k)
        num_digits = len(num)
        k_pointer = length_k - 1
        digits_pointer = num_digits - 1
        carry_over = 0
        curr_answer = []
        while k_pointer > -1 or digits_pointer > -1:
            if k_pointer == -1:
                if num[digits_pointer] + carry_over >= 10:
                    curr_answer.insert(0, num[digits_pointer] + carry_over - 10)
                    carry_over = 1
                else:
                    curr_answer.insert(0, num[digits_pointer] + carry_over)
                    carry_over = 0
                digits_pointer -= 1
            elif digits_pointer == -1:
                if int(string_k[k_pointer]) + carry_over >= 10:
                    curr_answer.insert(0, int(string_k[k_pointer]) + carry_over - 10)
                    carry_over = 1
                else:
                    curr_answer.insert(0, int(string_k[k_pointer]) + carry_over)
                    carry_over = 0
                k_pointer -= 1
            else:
                if int(string_k[k_pointer]) + num[digits_pointer] + carry_over >= 10:
                    curr_answer.insert(0, int(string_k[k_pointer]) + num[digits_pointer] + carry_over - 10)
                    carry_over = 1
                else:
                    curr_answer.insert(0, int(string_k[k_pointer]) + num[digits_pointer] + carry_over)
                    carry_over = 0
                digits_pointer -= 1
                k_pointer -= 1
        if carry_over:
            curr_answer.insert(0, carry_over)
        return curr_answer