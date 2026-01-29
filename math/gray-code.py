class Solution:
    def grayCode(self, n: int) -> List[int]:
        # n = 3
        # 000, 001, 011, 010, 110, 111, 101, 100
        # [0, 1, 3, 2, 6, 4, 5, 7]
        # Take the previous iteration, add a new bit (1) at the beginning, then mirror
        prev = [0, 1]
        for i in range(1, n):
            new_answer = prev.copy()
            for j in range(pow(2, i) - 1, -1, -1):
                new_answer.append(prev[j] ^ (1 << i))
            prev = new_answer
        return prev
        