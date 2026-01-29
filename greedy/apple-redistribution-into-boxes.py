class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        num_apples = sum(apple)
        curr = 0
        for i in range(len(capacity) - 1, -1, -1):
            curr += capacity[i]
            if curr >= num_apples:
                return len(capacity) - i
        return len(capacity)