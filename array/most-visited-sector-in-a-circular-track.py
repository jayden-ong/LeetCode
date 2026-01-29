class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        num_revolutions = 0
        num_rounds = len(rounds)
        starting_pos = rounds[0]
        curr_pos = rounds[0]
        for i in range(1, num_rounds):
            # Made a full revolution if last pos is greater 
            if rounds[i - 1] > rounds[i]:
                num_revolutions += 1
            curr_pos = rounds[i]
        
        answer = []
        i = starting_pos
        while i != curr_pos:
            answer.append(i)
            i += 1
            if i > n:
                i = 1
        answer.append(curr_pos)
        answer.sort()
        return answer