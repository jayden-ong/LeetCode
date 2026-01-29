class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        dictionary = set()
        base = pow(10, (n - 1) // 2)
        is_odd = (n % 2 == 1)
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][is_odd:]
            s_int = int(s)
            if s_int % k == 0:
                dictionary.add("".join(sorted(s)))
        
        fact = []
        for i in range(n + 1):
            fact.append(factorial(i))
        answer = 0
        for s in dictionary:
            count = [0] * 10
            for c in s:
                count[int(c)] += 1
            total = (n - count[0]) * fact[n - 1]
            for x in count:
                total //= fact[x]
            answer += total
        return answer