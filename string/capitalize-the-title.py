class Solution:
    def capitalizeTitle(self, title: str) -> str:
        answer = ""
        for word in title.split(' '):
            new_word = word.lower()
            if len(word) > 2:
                answer += new_word[0].upper() + new_word[1:] + " "
            else:
                answer += new_word + " "

        return answer.rstrip()