class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column_dict = { 1 : "A",
                        2 : "B",
                        3 : "C",
                        4 : "D",
                        5 : "E",
                        6 : "F",
                        7 : "G",
                        8 : "H",
                        9 : "I",
                        10 : "J",
                        11 : "K",
                        12 : "L",
                        13 : "M",
                        14 : "N",
                        15 : "O",
                        16 : "P",
                        17 : "Q",
                        18 : "R",
                        19 : "S",
                        20 : "T",
                        21 : "U",
                        22 : "V",
                        23 : "W",
                        24 : "X",
                        25 : "Y",
                        26 : "Z",
                        }
        
        num_bits = 1
        curr_max = 26
        # Get the number of bits required
        while curr_max < columnNumber:
            curr_max = curr_max + pow(26, num_bits + 1)
            num_bits += 1
        
        curr_answer = ""
        curr_min = curr_max - pow(26, num_bits) + 1
        while num_bits > 0:
            # 5473578 -> 446842 -> 7442 -> 6
            # 475255 -> 18279 -> 703 -> 27
            curr_col = columnNumber // pow(26, num_bits - 1)
            # Took too much, have to decrease the current column number
            remainder = columnNumber - curr_col * pow(26, num_bits - 1)
            curr_min -= pow(26, num_bits - 1)
            if remainder < curr_min and num_bits > 1: 
                curr_col -= 1
                remainder += pow(26, num_bits - 1)
            letter_to_add = column_dict[curr_col]
            curr_answer += letter_to_add
            num_bits -= 1
            columnNumber = remainder
        
        return curr_answer