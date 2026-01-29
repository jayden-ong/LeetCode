class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7
        y_coord_to_point = defaultdict(int)
        for x, y in points:
            y_coord_to_point[y] +=1 
        
        answer = 0
        total_num_edges = 0
        for num_coords in y_coord_to_point.values():
            num_edges = (num_coords - 1) * num_coords // 2
            answer = (answer + num_edges * total_num_edges) % MOD
            total_num_edges = (total_num_edges + num_edges) % MOD
        return answer
        
