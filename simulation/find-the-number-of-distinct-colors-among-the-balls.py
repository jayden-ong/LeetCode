class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        num_unique = 0
        # Maps each ball to its color
        balls_to_color = defaultdict(int)
        # Contains the frequency of each color
        colors_dict = defaultdict(int)
        answer = []
        for ball, color in queries:
            if balls_to_color[ball] > 0:
                # It was set with a color previously
                colors_dict[balls_to_color[ball]] -= 1
                # We have no more of that color
                if colors_dict[balls_to_color[ball]] == 0:
                    num_unique -= 1

            balls_to_color[ball] = color
            colors_dict[color] += 1
            # It already existed previously if colors_dict[color] > 1
            if colors_dict[color] == 1:
                num_unique += 1
            answer.append(num_unique)
        return answer
        
