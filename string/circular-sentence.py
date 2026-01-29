class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_list = sentence.split(' ')
        sentence_length = len(sentence_list)
        for i in range(sentence_length):
            if i == 0:
                if sentence_list[0][0] != sentence_list[-1][-1]:
                    return False
            else:
                if sentence_list[i - 1][-1] != sentence_list[i][0]:
                    return False
        return True