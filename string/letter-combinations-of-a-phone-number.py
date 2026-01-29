from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_digits = len(digits)
        if num_digits == 0:
            return []
        
        curr_res = []
        digits_letters = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        for digit in digits:
            if curr_res == []:
                curr_res = digits_letters[digit]
            else:
                temp = []
                for a, b in product(curr_res, digits_letters[digit]):
                    temp.append(a + b)
                curr_res = temp
        return curr_res