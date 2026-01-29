MOD = 10**9 + 7
absolute_max = 10**5
fact_dict = [0] * absolute_max
inverse_fact_dict = [0] * absolute_max
def quick_power(x, n):
    answer = 1
    while n >= 1:
        if n & 1:
            answer = answer * x % MOD
        x = x * x % MOD
        n >>= 1
    return answer
        
def setup():
    if fact_dict[0] != 0:
        return
    fact_dict[0] = 1
    for i in range(1, absolute_max):
        fact_dict[i] = fact_dict[i - 1] * i % MOD
    inverse_fact_dict[absolute_max - 1] = quick_power(fact_dict[absolute_max - 1], MOD - 2)
    for i in range(absolute_max - 1, 0, -1):
        inverse_fact_dict[i - 1] = inverse_fact_dict[i] * i % MOD
        
def combination(n, m):
    return fact_dict[n] * inverse_fact_dict[m] % MOD * inverse_fact_dict[n - m] % MOD
    
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        setup()
        return combination(n - 1, k) * m % MOD * quick_power(m - 1, n - k - 1) % MOD