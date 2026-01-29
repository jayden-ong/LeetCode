class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(num):
            if num == 1:
                return False
            
            for i in range(2, int(pow(num, 0.5)) + 1):
                if num % i == 0:
                    return False
            return True

        num_rows = len(nums)
        num_cols = len(nums[0])
        answer = 0
        for i in range(num_rows):
            if nums[i][i] > answer:
                if is_prime(nums[i][i]):
                    answer = max(answer, nums[i][i])
            
            if nums[i][num_rows - i - 1] > answer:
                if is_prime(nums[i][num_rows - 1 - i]):
                    answer = max(answer, nums[i][num_cols - 1 - i])
        return answer