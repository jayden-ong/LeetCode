class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        nodes_dict = defaultdict(list)
        for x, y, time in meetings:
            nodes_dict[x].append((time, y))
            nodes_dict[y].append((time, x))
        
        knows_secret = [float('inf')] * n
        knows_secret[0], knows_secret[firstPerson] = 0, 0

        secret_queue = deque()
        secret_queue.append((0, 0))
        secret_queue.append((firstPerson, 0))
        while secret_queue:
            curr_person, curr_time = secret_queue.popleft()
            if curr_time > knows_secret[curr_person]:
                continue
            
            for next_time, next_person in nodes_dict[curr_person]:
                # If the next person knows the secret earlier, we have to check all of their meetings again
                if next_time >= curr_time and knows_secret[next_person] > next_time:
                    knows_secret[next_person] = next_time
                    secret_queue.append((next_person, next_time))

        return [i for i in range(n) if knows_secret[i] != float('inf')]