class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        answer = target[0]
        # The amount of operations required to fix a mountain is equal to its peak
        # If the next num is smaller, we can include it in one of the previous operations
        # When we find a new peak, we need a new operation because the connection
        # to the previous peak would be cut off
        for i in range(1, len(target)):
            answer += max(target[i] - target[i - 1], 0)
        return answer