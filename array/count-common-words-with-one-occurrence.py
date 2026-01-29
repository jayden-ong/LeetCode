class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        answer = 0
        answer1_dict = {}
        answer2_dict = {}
        for word in words1:
            if word in answer1_dict:
                answer1_dict[word] += 1
            else:
                answer1_dict[word] = 1
        
        for word in words2:
            if word in answer2_dict:
                answer2_dict[word] += 1
            else:
                answer2_dict[word] = 1
        
        for word in answer1_dict:
            if answer1_dict[word] == 1 and word in answer2_dict and answer2_dict[word] == 1:
                answer += 1
        return answer