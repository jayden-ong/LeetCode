class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:
            curr_res = x
            negative = False
            if n < 0:
                negative = True
            
            num_multiplied = 1
            total_multiplied = 0
            curr_storage = 1
            absolute_n = abs(n)
            while total_multiplied < absolute_n:
                if total_multiplied + (num_multiplied * 2) > absolute_n:
                    curr_storage *= curr_res
                    curr_res = x
                    total_multiplied += num_multiplied
                    num_multiplied = 1
                else:
                    curr_res *= curr_res
                    num_multiplied *= 2
            
            if negative:
                return 1/curr_storage
            return curr_storage