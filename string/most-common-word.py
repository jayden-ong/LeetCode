class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        length_paragraph = len(paragraph)
        curr_begin = 0
        most_common = None
        most_frequent = -1
        words_dict = {}
        i = 0
        while i < length_paragraph:
            if paragraph[i] in " !?',;.":
                curr_word = paragraph[curr_begin:i].lower()
                if curr_word in words_dict:
                    words_dict[curr_word] += 1
                else:
                    words_dict[curr_word] = 1
                
                if words_dict[curr_word] > most_frequent and curr_word not in banned:
                    most_common = curr_word
                    most_frequent = words_dict[curr_word]
                
                curr_begin = i + 1
                while curr_begin < length_paragraph and paragraph[curr_begin] in " !?',;.":
                    curr_begin += 1
                i = curr_begin 
            else:
                i += 1

        if curr_begin != length_paragraph:
            curr_word = paragraph[curr_begin:].lower()
            if curr_word in words_dict:
                words_dict[curr_word] += 1
            else:
                words_dict[curr_word] = 1
                
            if words_dict[curr_word] > most_frequent and curr_word not in banned:
                most_common = curr_word
                most_frequent = words_dict[curr_word]
        #print(word_dict)
        return most_common