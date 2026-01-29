class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        string_x = str(format(x, "b"))
        string_y = str(format(y, "b"))
        num_bits_x = len(string_x)
        num_bits_y = len(string_y)
        i = num_bits_x - 1
        j = num_bits_y - 1
        num_diff = 0
        while i > -1 or j > -1:
            if i == -1:
                if string_y[j] != '0':
                    num_diff += 1
                j -= 1
            elif j == -1:
                if string_x[i] != '0':
                    num_diff += 1
                i -= 1
            else:
                if string_x[i] != string_y[j]:
                    num_diff += 1
                i -= 1
                j -= 1
        return num_diff
        