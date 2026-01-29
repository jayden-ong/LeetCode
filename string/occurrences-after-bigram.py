class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_list = text.split(" ")
        num_words = len(text_list)
        answer = []
        for i in range(2, num_words):
            if text_list[i - 2] == first and text_list[i - 1] == second:
                answer.append(text_list[i])
        return answer