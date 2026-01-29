class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MODULO = (10 ** 9) + 7
        num_even_indices = n // 2
        if n % 2 == 1:
            num_even_indices += 1
        
        def custom_pow(base, exponent):
            answer = 1
            curr_base = base
            while exponent > 0:
                if exponent % 2 == 1:
                    answer = answer * curr_base % MODULO
                    exponent -= 1
                
                curr_base = curr_base * curr_base % MODULO
                exponent //= 2
            return answer

        # There are 5 possible options for all even indices
        return (custom_pow(5, num_even_indices) * custom_pow(4, n - num_even_indices)) % MODULO