class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length_str1 = len(str1)
        length_str2 = len(str2)

        if length_str1 < length_str2:
            min_length = length_str1
            shortest_string = str1
            other_string = str2
            other_min_length = length_str2
        else:
            min_length = length_str2
            shortest_string = str2
            other_string = str1
            other_min_length = length_str1
        
        curr = ""
        curr_length = 0
        curr_longest = ""
        for char in shortest_string:
            curr += char
            curr_length += 1
            min_num_repetitions = min_length // curr_length
            num_repetitions = other_min_length // curr_length
            #print(curr)
            #print(min_num_repetitions)
            #print(min_num_repetitions * curr_length)
            #print(num_repetitions)
            #print(num_repetitions * curr_length)
            if min_num_repetitions * curr == shortest_string and num_repetitions * curr == other_string:
                curr_longest = curr
        return curr_longest