class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        num_words = len(words)
        sentence = [0] * num_words 
        for word in words:
            sentence[int(word[-1]) - 1] = word
        
        answer = ""
        for word in sentence:
            answer += word[:-1] + " "
        return answer.rstrip()