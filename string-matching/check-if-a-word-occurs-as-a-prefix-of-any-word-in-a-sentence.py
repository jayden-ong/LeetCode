class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words_list = sentence.split(' ')
        length_search = len(searchWord)
        for i in range(len(words_list)):
            if searchWord == words_list[i][:length_search]:
                return i + 1
        return -1