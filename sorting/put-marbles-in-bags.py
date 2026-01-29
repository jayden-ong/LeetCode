class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # index 0 and len(weights) - 1 will always be part of the weights
        # We need to choose k - 1 splitting points
        # For each splitting point, the first point will form a bag with the last point of the prev splitting point
        splitting_points = []
        for i in range(len(weights) - 1):
            splitting_points.append(weights[i] + weights[i + 1])
        
        splitting_points.sort()
        answer = 0
        for i in range(k - 1):
            answer += splitting_points[len(splitting_points) - i - 1] - splitting_points[i]
        return answer