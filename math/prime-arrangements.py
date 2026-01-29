from math import factorial
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # Number of composites factorial multiplied by number of primes factorial
        def determine_prime(num):
            for i in range(2, int(num ** (0.5) + 1)):
                if num % i == 0:
                    return False
            return True

        num_prime = 0
        num_not_prime = 0
        for i in range(1, n + 1):
            if i == 1:
                num_not_prime += 1
            elif i == 2:
                num_prime += 1
            else:
                if determine_prime(i):
                    num_prime += 1
                else:
                    num_not_prime += 1
        return (factorial(num_prime) * factorial(num_not_prime)) % (10 ** 9 + 7)