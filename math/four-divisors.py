class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def find_divisors(num):
            divisors = set()
            for i in range(1, math.ceil(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(num // i)
                    divisors.add(i)
            
            if len(divisors) == 4:
                return sum(divisors)
            return 0
        
        answer = 0
        for num in nums:
            answer += find_divisors(num)
        return answer