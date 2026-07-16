class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        curr = 0
        for i, num in enumerate(nums):
            if i == 0:
                prefix_gcd.append(num)
                curr = num
            else:
                curr = max(curr, num)
                prefix_gcd.append(math.gcd(num, curr))
        
        prefix_gcd.sort()
        answer = 0
        for i in range(len(prefix_gcd) // 2):
            if i == len(prefix_gcd) - 1 - i:
                break
            answer += math.gcd(prefix_gcd[i], prefix_gcd[len(prefix_gcd) - i - 1])
        return answer