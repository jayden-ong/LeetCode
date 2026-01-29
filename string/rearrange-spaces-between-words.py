class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_spaces = text.count(' ')
        curr_word = ""
        words_list = []
        num_words = 0
        for char in text:
            if char == " " and curr_word != "":
                words_list.append(curr_word)
                curr_word = ""
                num_words += 1
            elif char != " ":
                curr_word += char
        
        if curr_word != "":
            words_list.append(curr_word)
            num_words += 1
        
        spaces_between = 0
        remaining_space = num_spaces
        if num_words != 1:
            spaces_between = num_spaces // (num_words - 1)
            remaining_space = num_spaces % (num_words - 1)
        answer = ""
        #print(spaces_between)
        #print(remaining_space)
        for word in words_list:
            answer += word + " " * spaces_between
        answer = answer.rstrip()
        answer += " " * remaining_space
        return answer