class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Things to try:
        # Don't get the length of num
        #      Doesn't work because we need to know if we can return early when k = len
        # Keep track of the smallest ever digit to break out of for loop
        # num_digits = len(num)
        num_digits = 0
        actual_smallest = 10
        for digit in num:
            num_digits += 1
            actual_smallest = min(int(digit), actual_smallest)

        max_length = num_digits - k
        if max_length == 0:
            return "0"
        
        curr_starting_point = 0
        curr_string = ""
        # join will convert from list to a string
        while num_digits != max_length and max_length != 0:
            smallest_index = curr_starting_point
            smallest_index_val = int(num[curr_starting_point])
            if smallest_index_val != actual_smallest:
                for i in range(1 + curr_starting_point, num_digits - (max_length - 1) + curr_starting_point):
                    curr_num = int(num[i])
                    if smallest_index_val > curr_num:
                        smallest_index_val = curr_num
                        smallest_index = i
                        if smallest_index_val == actual_smallest:
                            break

            curr_string += num[smallest_index]
            num_digits = num_digits - smallest_index - 1 + curr_starting_point
            max_length -= 1
            curr_starting_point = smallest_index + 1
        
        curr_result = curr_string + num[curr_starting_point:curr_starting_point + max_length]
        curr_result = curr_result.lstrip('0')
        if curr_result == "":
            return "0"
        return curr_result
