class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = pow(10, 9) + 7
        nums_prime_factors = [0] * len(nums)
        for i in range(len(nums)):
            num = nums[i]
            for j in range(2, int(pow(nums[i], 0.5)) + 1):
                if num % j == 0:
                    nums_prime_factors[i] += 1
                
                while num % j == 0:
                    num //= j
            
            if num >= 2:
                nums_prime_factors[i] += 1
        
        index_more_factors = [len(nums)] * len(nums)
        index_more_factors_rev = [-1] * len(nums)
        curr_heap = []
        nums_heap = []
        for i in range(len(nums)):
            while(curr_heap and nums_prime_factors[curr_heap[-1]] < nums_prime_factors[i]):
                index_more_factors[curr_heap.pop()] = i
            
            if curr_heap:
                index_more_factors_rev[i] = curr_heap[-1]
            
            curr_heap.append(i)
            # for later
            heapq.heappush(nums_heap, (-nums[i], i))
        
        def power(base, exponent):
            res = 1

            # Calculate the exponentiation using binary exponentiation
            while exponent > 0:
                # If the exponent is odd, multiply the result by the base
                if exponent % 2 == 1:
                    res *= base
                    res %= pow(10, 9) + 7

                # Square the base and halve the exponent
                base *= base
                base %= pow(10, 9) + 7
                exponent //= 2

            return res
        
        answer = 1
        while k > 0:
            # Pick the largest number
            curr_largest, curr_index = heapq.heappop(nums_heap)
            curr_largest *= -1

            sub_length = min((index_more_factors[curr_index] - curr_index) * (curr_index - index_more_factors_rev[curr_index]) , k)
            
            answer *= power(curr_largest, sub_length)
            answer %= mod
            k -= sub_length
        return answer