class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        answer = []
        def find_longest_suffix(query_word, container_word, starting_index):
            query_word_r, container_word_r = query_word[::-1], container_word[::-1]
            # No point since we have already found a longer match
            if starting_index > len(query_word):
                return 0
            
            for i in range(max(0, starting_index - 1), min(len(container_word), len(query_word))):
                if query_word_r[:i + 1] != container_word_r[:i + 1]:
                    return i
            return min(len(query_word), len(container_word))


        for word in wordsQuery:
            longest_suffix_length, answer_index = 0, -1
            for i, possible_answer in enumerate(wordsContainer):
                suffix_length = find_longest_suffix(word, possible_answer, longest_suffix_length)
                if answer_index == -1 or suffix_length > longest_suffix_length:
                    longest_suffix_length, answer_index = suffix_length, i
                elif suffix_length == longest_suffix_length and len(wordsContainer[i]) < len(wordsContainer[answer_index]):
                    answer_index = i
            answer.append(answer_index)
                    
        return answer