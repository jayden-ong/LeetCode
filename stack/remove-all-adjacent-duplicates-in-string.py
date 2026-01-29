class Solution:
    def removeDuplicates(self, s: str) -> str:
        curr_string = s
        length_s = len(s)
        i = 1
        while i < length_s:
            if curr_string[i - 1] == curr_string[i]:
                length_s -= 2
                curr_string = curr_string[:i - 1] + curr_string[i + 1:]
                if i == 1:
                    i = 1
                else:
                    i -= 1
            else:
                i += 1
        return curr_string