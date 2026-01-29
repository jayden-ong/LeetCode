class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_index = 0
        curr_pos = [0, 0]
        obstacles_set = set()
        max_distance = 0
        for obstacle in obstacles:
            obstacles_set.add(tuple(obstacle))
        
        for command in commands:
            if command == -1:
                curr_index += 1
                if curr_index >= 4:
                    curr_index = 0
            elif command == -2:
                curr_index -= 1
                if curr_index < 0:
                    curr_index = 3
            else:
                for i in range(command):
                    curr_pos[0], curr_pos[1] = curr_pos[0] + directions[curr_index][0], curr_pos[1] + directions[curr_index][1]
                    if tuple(curr_pos) in obstacles_set:
                        curr_pos[0], curr_pos[1] = curr_pos[0] - directions[curr_index][0], curr_pos[1] - directions[curr_index][1]
                        break
                    max_distance = max((curr_pos[0] ** 2) + (curr_pos[1] ** 2), max_distance)
        return max_distance