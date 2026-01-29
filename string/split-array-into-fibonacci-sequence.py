class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def make_choice(curr_index, curr_answer, curr_num):
            if curr_index == len(num):
                if curr_num == "" and len(curr_answer) >= 3:
                    return curr_answer
                return []

            # At each index, can choose to add num[curr_index] to curr_num
            # Can only do this if num[curr_index] is not 0 and curr_num != ""
            # It would mean it was a leading 0
            first_option = []
            if curr_num != "" or num[curr_index] != '0':
                temp = curr_answer.copy()
                first_option = make_choice(curr_index + 1, curr_answer, curr_num + num[curr_index])
                if first_option != []:
                    return first_option
                curr_answer = temp
            
            # Other option is to append it to our answer
            temp = curr_answer.copy()
            second_option = []
            if (len(curr_answer) < 2 or int(curr_num + num[curr_index]) == curr_answer[-1] + curr_answer[-2]) and int(curr_num + num[curr_index]) < pow(2, 31):
                curr_answer.append(int(curr_num + num[curr_index]))
                second_option = make_choice(curr_index + 1, curr_answer, "")
                if second_option != []:
                    return second_option
                curr_answer = temp
            
            return []

        return make_choice(0, [], "")