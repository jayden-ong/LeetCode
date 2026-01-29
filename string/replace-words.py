class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        new_sentence = ""
        for word in words:
            curr_word = ""
            for short in dictionary:
                short_len = len(short)
                if word[:short_len] == short:
                    if curr_word == "" or len(curr_word) > short_len:
                        curr_word = short
            if curr_word == "":
                new_sentence += word + " "
            else:
                new_sentence += curr_word + " "
        return new_sentence.strip()
