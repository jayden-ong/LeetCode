class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        answer = 0
        num_even = 0
        num_odd = 0
        for num in arr:
            if num % 2 == 0:
                answer += num_odd
                num_even += 1
            else:
                answer += num_even + 1
                num_odd, num_even = num_even, num_odd
                num_odd += 1

        return answer % (pow(10, 9) + 7)