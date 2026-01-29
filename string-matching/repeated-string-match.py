class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # First, "a" must be repeated enough to be as long as "b"
        new_a = a
        answer = 1
        while len(new_a) < len(b):
            new_a += a
            answer += 1
        
        if b in new_a:
            return answer
        elif b in (new_a + a):
            return answer + 1
        
        return -1