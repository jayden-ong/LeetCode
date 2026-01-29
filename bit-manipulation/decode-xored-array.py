class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        answer = [first]
        curr = first
        for item in encoded:
            curr ^= item
            answer.append(curr)
        return answer