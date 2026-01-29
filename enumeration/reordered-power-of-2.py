class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        string_n = str(n)
        def valid(curr_num):
            n_dict = defaultdict(int)
            for digit in string_n:
                n_dict[digit] += 1
            
            string_num = str(curr_num)
            if len(string_num) != len(string_n):
                return False
            
            for digit in string_num:
                if n_dict[digit] > 0:
                    n_dict[digit] -= 1
                else:
                    return False
            return True

        cap = 10 ** 9
        curr = 1
        while curr <= cap:
            if valid(curr):
                return True
            curr *= 2
        return False