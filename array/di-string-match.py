class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left = 0
        right = len(s)
        answer = []
        for char in s:
            if char == "I":
                answer.append(left)
                left += 1
            else:
                answer.append(right)
                right -= 1
        answer.append(left)
        return answer