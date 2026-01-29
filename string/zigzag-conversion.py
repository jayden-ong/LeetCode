class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        string_length = len(s)
        new_string = ""
        skipping_index = 2 * numRows - 2
        curr_sub = skipping_index - 2
        for k in range(numRows):
            # Get first line
            if k == 0 or k == numRows - 1:
                for i in range(k, string_length, skipping_index):
                    new_string += s[i]
            else:
                for j in range(k, string_length, skipping_index):
                    new_string += s[j]
                    if j + curr_sub < string_length:
                        new_string += s[j + curr_sub]
                curr_sub -= 2
        return new_string