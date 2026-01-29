class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence_split = sentence.split(" ")
        goat_latin = ""
        i = 1
        for word in sentence_split:
            if word[0] in 'aeiouAEIOU':
                goat_latin = goat_latin + word + "ma" + (i * "a") + " "
            else:
                goat_latin = goat_latin + word[1:] + word[0] + "ma" + (i * "a") + " "
            i += 1

        return goat_latin.rstrip()