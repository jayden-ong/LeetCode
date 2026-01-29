class Solution:
    def countValidWords(self, sentence: str) -> int:
        answer = 0
        curr_string = ""
        num_hyphens = 0
        num_punctuation = 0
        is_valid = True
        sentence_length = len(sentence)
        for i in range(sentence_length):
            if sentence[i] == " ":
                if curr_string != "" and is_valid:
                    answer += 1
                num_hyphens = 0
                num_punctuation = 0
                curr_string = ""
                is_valid = True
            else:
                curr_string += sentence[i]
                if sentence[i] == "-":
                    num_hyphens += 1
                    if i == 0 or i == sentence_length - 1 or sentence[i - 1] not in 'abcdefghijklmnopqrstuvwxyz' or sentence[i + 1] not in 'abcdefghijklmnopqrstuvwxyz':
                        is_valid = False
                
                if sentence[i] in "!.,":
                    num_punctuation += 1
                    # Punctuation is not last token
                    if i < sentence_length - 1 and sentence[i + 1] != " ":
                        is_valid = False
                
                if num_punctuation > 1 or num_hyphens > 1 or sentence[i].isnumeric():
                    is_valid = False

        if is_valid and curr_string != "":
            answer += 1
        return answer