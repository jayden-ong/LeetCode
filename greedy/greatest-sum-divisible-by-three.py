class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        answer = sum(nums)
        remainder = answer % 3
        if remainder == 0:
            return answer
        
        smallest_remainder_one, second_smallest_remainder_one = float('inf'), float('inf')
        smallest_remainder_two, second_smallest_remainder_two = float('inf'), float('inf')
        for num in nums:
            if num % 3 == 1:
                if smallest_remainder_one == float('inf') or num < smallest_remainder_one:
                    smallest_remainder_one, second_smallest_remainder_one = num, smallest_remainder_one
                elif second_smallest_remainder_one == float('inf') or num < second_smallest_remainder_one:
                    second_smallest_remainder_one = num
            elif num % 3 == 2:
                if smallest_remainder_two == float('inf') or num < smallest_remainder_two:
                    smallest_remainder_two, second_smallest_remainder_two = num, smallest_remainder_two
                elif second_smallest_remainder_two == float('inf') or num < second_smallest_remainder_two:
                    second_smallest_remainder_two = num
        
        smallest = float('inf')
        if remainder == 1:
            if smallest_remainder_one != float('inf'):
                smallest = min(smallest, smallest_remainder_one)
            if smallest_remainder_two != float('inf') and second_smallest_remainder_two != float('inf'):
                smallest = min(smallest, smallest_remainder_two + second_smallest_remainder_two)
            
            if smallest == float('inf'):
                return 0
        elif remainder == 2:
            if smallest_remainder_two != float('inf'):
                smallest = min(smallest, smallest_remainder_two)
            if smallest_remainder_one != float('inf') and second_smallest_remainder_one != float('inf'):
                smallest = min(smallest, smallest_remainder_one + second_smallest_remainder_one)
            
            if smallest == float('inf'):
                return 0
        return answer - smallest