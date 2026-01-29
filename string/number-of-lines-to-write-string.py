class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        temp = "abcdefghijklmnopqrstuvwxyz"
        letters_dict = {}
        for i in range(26):
            letters_dict[temp[i]] = widths[i]
        # print(letters_dict)

        num_lines = 1
        length_s = len(s)
        space_on_line = 100
        for i in range(length_s):
            # There is enough space to write on current line
            if space_on_line >= letters_dict[s[i]]:
                space_on_line -= letters_dict[s[i]]
            else:
                num_lines += 1
                space_on_line = 100 - letters_dict[s[i]]
        return [num_lines, 100 - space_on_line]