class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) == len(sentence2):
            return sentence1 == sentence2
        
        def find_word(sentence_list, word):
            for i in range(len(sentence_list)):
                if sentence_list[i] == word:
                    return i
            return -1
        
        sentence1_list = sentence1.split(' ')
        sentence2_list = sentence2.split(' ')
        one_is_shorter = len(sentence1_list) < len(sentence2_list)
        sentence1_index = 0
        sentence2_index = 0
        while sentence1_index < len(sentence1_list) and sentence2_index < len(sentence2_list):
            if sentence1_list[sentence1_index] != sentence2_list[sentence2_index]:
                if one_is_shorter:
                    for i in range(sentence2_index, len(sentence2_list)):
                        if sentence2_list[i:] == sentence1_list[sentence1_index:]:
                            return True
                    return False
                else:
                    for i in range(sentence1_index, len(sentence1_list)):
                        if sentence1_list[i:] == sentence2_list[sentence2_index:]:
                            return True
                    return False
            sentence1_index += 1
            sentence2_index += 1

        return True