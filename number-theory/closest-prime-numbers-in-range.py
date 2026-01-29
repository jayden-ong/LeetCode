class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime_list = [True] * (right + 1)
        prime_list[0] = False
        prime_list[1] = False
        def sieve():
            for i in range(2, int(pow(right, 0.5)) + 1):
                if prime_list[i]:
                    for num in range(i * i, right + 1, i):
                        prime_list[num] = False
        sieve()
        primes = []
        for index in range(left, right + 1):
            if prime_list[index]:
                primes.append(index)
        
        if len(primes) < 2:
            return [-1, -1]
        answer = [-1, -1]
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] <= 2:
                return [primes[i], primes[i + 1]]
            elif (answer[0] == -1 and answer[1] == -1) or primes[i + 1] - primes[i] < answer[1] - answer[0]:
                answer = [primes[i], primes[i + 1]]
            
        return answer