class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = pow(10, 9) + 7
        digit_sum = 0
        frequency = [0] * 10
        for i in range(len(num)):
            digit_sum += int(num[i])
            frequency[int(num[i])] += 1
        
        if digit_sum % 2 == 1:
            return 0
        
        target = digit_sum // 2
        num_odd = (len(num) + 1) // 2
        dp = [[0] * (num_odd + 1) for _ in range(target + 1)]
        dp[0][0] = 1
        possible_sum = total_sum = 0
        for i in range(10):
            possible_sum += frequency[i]
            total_sum += i * frequency[i]
            for odd_count in range(min(possible_sum, num_odd), max(0, possible_sum - (len(num) - num_odd)) - 1, -1):
                even_count = possible_sum - odd_count
                for curr in range(min(total_sum, target), max(0, total_sum - target) - 1, -1):
                    answer = 0
                    for j in range(max(0, frequency[i] - even_count), min(frequency[i], odd_count) + 1):
                        if i * j > curr:
                            break
                        
                        ways = (comb(odd_count, j) * comb(even_count, frequency[i] - j) % MOD)
                        answer = (answer + ways * dp[curr - i * j][odd_count - j] % MOD) % MOD
                    dp[curr][odd_count] = answer % MOD
        return dp[target][num_odd]
