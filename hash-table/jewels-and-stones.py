class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for char in stones:
            if char in jewels:
                answer += 1
        return answer