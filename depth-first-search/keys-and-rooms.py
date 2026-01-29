from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_visited = set()
        queue = deque()
        queue.append(0)
        rooms_visited.add(0)
        while queue:
            curr_room = queue.popleft()
            for key in rooms[curr_room]:
                if key not in rooms_visited:
                    rooms_visited.add(key)
                    queue.append(key)
            
            if len(rooms_visited) == len(rooms):
                return True
        return False