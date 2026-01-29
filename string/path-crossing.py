class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locations_visited = set()
        curr_location = (0,0)
        locations_visited.add(curr_location)
        for char in path:
            if char == "N":
                curr_location = (curr_location[0], curr_location[1] + 1)
            elif char == "S":
                curr_location = (curr_location[0], curr_location[1] - 1)
            elif char == "E":
                curr_location = (curr_location[0] - 1, curr_location[1])
            else:
                curr_location = (curr_location[0] + 1, curr_location[1])
            
            if curr_location in locations_visited:
                return True
            else:
                locations_visited.add(curr_location)
        return False