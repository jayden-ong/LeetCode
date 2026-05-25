class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        jump_locations_dict = {}
        jump_locations_list = []
        for i, char in enumerate(s):
            if char == "0":
                jump_locations_list.append(i)
                jump_locations_dict[i] = len(jump_locations_list) - 1
        
        visited = set()
        visited.add(0)
        queue = deque()
        queue.append(0)
        while queue:
            i = queue.popleft()
            if i == len(s) - 1:
                return True
            
            jump_location_index = jump_locations_dict[i]
            for k in range(jump_location_index + 1, len(jump_locations_list)):
                j = jump_locations_list[k]
                if i + minJump > j:
                    continue
                elif j > min(i + maxJump, len(s) - 1):
                    break
                else:
                    if j not in visited:
                        visited.add(j)
                        queue.append(j)
        return False
        