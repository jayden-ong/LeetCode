class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        def find_factors(num):
            i = 1
            res = []
            while i <= pow(num, 1/2):
                if num % i == 0 and i * i != num:
                    res.append(num // i)
                    res.append(i)
                elif num % i == 0 and i * i == num:
                    res.append(i)
                i += 1
            return res
        
        factors = find_factors(num)
        curr_res = 0
        for factor in factors:
            curr_res += factor
        curr_res -= num
        return curr_res == num