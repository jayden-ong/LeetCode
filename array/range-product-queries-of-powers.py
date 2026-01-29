class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        curr = n
        powers = []
        while curr > 0:
            largest_power = int(math.log(curr, 2))
            res = 2 ** largest_power
            powers.append(res)
            curr -= res
        powers = powers[::-1]
        prefix_mult = []
        curr = 1
        for num in powers:
            curr *= num
            prefix_mult.append(curr)
        
        answer = []
        for left, right in queries:
            divisor = 1
            if left > 0:
                divisor = prefix_mult[left - 1]
            
            answer.append(prefix_mult[right] // divisor % MOD)
        return answer