from collections import deque
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        reverse_edges_dict = defaultdict(int)
        for guest in range(len(favorite)):
            reverse_edges_dict[favorite[guest]] += 1
        
        guest_queue = deque()
        for person in range(len(favorite)):
            if reverse_edges_dict[person] == 0:
                guest_queue.append(person)
        
        max_length = [1] * len(favorite)
        while guest_queue:
            # Once you hit a node, it is at its max_length
            curr_guest = guest_queue.popleft()
            next_guest = favorite[curr_guest]
            max_length[next_guest] = max(max_length[next_guest], max_length[curr_guest] + 1)
            reverse_edges_dict[next_guest] -= 1
            if reverse_edges_dict[next_guest] == 0:
                guest_queue.append(next_guest)
        
        answer = 0
        two_length_cycles = 0
        for guest in range(len(favorite)):
            if reverse_edges_dict[guest] > 0:
                curr_length = 0
                curr_guest = guest
                while reverse_edges_dict[curr_guest] > 0:
                    reverse_edges_dict[curr_guest] = 0
                    curr_length += 1
                    curr_guest = favorite[curr_guest]
                
                if curr_length == 2:
                    # Can combine sequence of two-length cycles chains
                    two_length_cycles += max_length[guest] + max_length[favorite[guest]]
                else:
                    answer = max(answer, curr_length)
        return max(answer, two_length_cycles)