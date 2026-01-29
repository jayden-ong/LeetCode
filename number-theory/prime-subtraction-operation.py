class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        all_primes = []
        for i in range(2, 1001):
            is_prime = True
            end_loop = int(pow(i, 1/2)) + 1
            for j in range(2, end_loop):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                all_primes.append(i)
        
        curr_index = 0
        for i in range(len(nums)):
            if i == 0:
                curr_best = None
                for prime in all_primes:
                    if prime >= nums[i]:
                        break
                    else:
                        curr_best = prime
                
                if curr_best is not None:
                    nums[i] -= curr_best
            else:
                lower_bound = nums[i - 1]
                curr_best = None
                for prime in all_primes:
                    if prime >= nums[i]:
                        break
                    elif nums[i] - prime > lower_bound:
                        curr_best = prime
                
                if curr_best is not None:
                    nums[i] -= curr_best
                
                if nums[i] <= lower_bound:
                    return False
        return True
