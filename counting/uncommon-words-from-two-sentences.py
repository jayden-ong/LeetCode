class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split(" ")
        s2_words = s2.split(" ")
        words_dict = {}
        for word in s1_words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        
        for word in s2_words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        
        answer = []
        for key in words_dict:
            if words_dict[key] == 1:
                answer.append(key)
        return answer