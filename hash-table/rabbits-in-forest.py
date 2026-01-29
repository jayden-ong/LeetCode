class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Anyone that answers the same could have the same color if the number that answered it is at most what they say
        # If three rabbits answer 1, they can't all be the same color
        answer_dict = {}
        for answer in answers:
            if answer in answer_dict:
                answer_dict[answer] += 1
            else:
                answer_dict[answer] = 1
        
        # Three rabbits can all be the same color and say 2
        curr = 0
        for answer in answer_dict:
            num_answers = answer_dict[answer]
            if answer >= num_answers - 1:
                curr += answer + 1
            else:
                if answer == 0:
                    curr += num_answers
                else:
                    curr += (num_answers // (answer + 1)) * (answer + 1)
                    if (num_answers % (answer + 1)) != 0:
                        curr += answer + 1
        return curr