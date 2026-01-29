from collections import deque
class Solution:
    def soupServings(self, n: int) -> float:
        answers_dict = {}
        def serve_soup(curr_a, curr_b):
            if curr_a == 0 and curr_b == 0:
                return 0.5
            elif curr_a == 0:
                return 1
            elif curr_b == 0:
                return 0
            elif (curr_a, curr_b) in answers_dict:
                return answers_dict[curr_a, curr_b]
            
            answer = 0
            # Option A
            answer += 0.25 * serve_soup(max(curr_a - 100, 0), curr_b)
            # Option B
            answer += 0.25 * serve_soup(max(curr_a - 75, 0), max(curr_b - 25, 0))
            # Option C
            answer += 0.25 * serve_soup(max(curr_a - 50, 0), max(curr_b - 50, 0))
            # Option D
            answer += 0.25 * serve_soup(max(curr_a - 25, 0), max(curr_b - 75, 0))
            answers_dict[(curr_a, curr_b)] = answer
            return answer
        
        if n > 4500:
            return 1
        return serve_soup(n, n)