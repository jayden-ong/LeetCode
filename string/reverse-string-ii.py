class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length_s = len(s)
        # Reverse the first "k" characters for every sequence of 2k characters
        curr_string = ""
        curr_string_length = 0
        # Num characters should not change
        while curr_string_length < length_s:
            string_to_reverse = s[curr_string_length:curr_string_length + k]
            if len(string_to_reverse) < k:
                curr_string += string_to_reverse[::-1]
            else:
                string_stay_same = s[curr_string_length + k:curr_string_length + 2 * k]
                curr_string = curr_string + string_to_reverse[::-1] + string_stay_same
            curr_string_length += 2 * k
        return curr_string