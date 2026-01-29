class Solution:
    def minSteps(self, n: int) -> int:
        num_a = 1
        answer = 0
        num_copy = 1
        while num_a != n:
            # Can only copy again if the number of items we are copying is a multiple of however many we need
            num_leftover = n - num_a
            # We can copy it
            if num_leftover % num_a == 0:
                num_copy = num_a
                num_a += num_copy
                answer += 1
            else:
                num_a += num_copy
            answer += 1

        return answer