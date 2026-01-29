class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        directions = ["NW", "NE", "SW", "SE"]
        answer = 0
        for direction in directions:
            curr_answer = 0
            curr_distance = 0
            curr_k = k
            for char in s:
                if char == direction[0] or char == direction[1]:
                    curr_distance += 1
                else:
                    if curr_k > 0:
                        curr_k -= 1
                        curr_distance += 1
                    else:
                        curr_distance -= 1
                curr_answer = max(curr_answer, curr_distance)
            answer = max(answer, curr_answer)
        return answer