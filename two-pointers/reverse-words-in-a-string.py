class Solution:
    def reverseWords(self, s: str) -> str:
        curr_sentence = ""
        s = s.strip()
        curr_word = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if curr_word != "":
                    curr_sentence += curr_word[::-1] + " "
                    curr_word = ""
            else:
                curr_word += s[i]
        
        if curr_word != "":
            curr_sentence += curr_word[::-1]
        return curr_sentence.strip()