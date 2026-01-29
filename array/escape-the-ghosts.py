class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # If the ghosts can reach the target before you, you lose
        distance_to_target = abs(target[0]) + abs(target[1])
        for ghost_0, ghost_1 in ghosts:
            ghost_distance = abs(target[0] - ghost_0) + abs(target[1] - ghost_1)
            if ghost_distance <= distance_to_target:
                return False
        
        return True