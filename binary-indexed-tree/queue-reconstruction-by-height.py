class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        num_people = len(people)
        answer = [0] * len(people)
        heapq.heapify(people)
        while people:
            curr_height, curr_front = heapq.heappop(people)
            # For the shortest person, curr_front people need to be in front
            # Their position would be answer[curr_front]
            num_people_in_front = curr_front
            for i in range(len(answer)):
                if answer[i] == 0:
                    if num_people_in_front == 0:
                        answer[i] = [curr_height, curr_front]
                        break
                    num_people_in_front -= 1
                else:
                    if answer[i][0] == curr_height:
                        num_people_in_front -= 1
        return answer