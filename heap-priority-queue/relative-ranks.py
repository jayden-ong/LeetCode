class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = score.copy()
        sorted_score.sort(reverse=True)
        scores_dict = {}
        i = 1
        for rank in sorted_score:
            scores_dict[rank] = i
            i += 1
        
        answer = []
        for key in score:
            if scores_dict[key] == 1:
                answer.append("Gold Medal")
            elif scores_dict[key] == 2:
                answer.append("Silver Medal")
            elif scores_dict[key] == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(scores_dict[key]))
        return answer