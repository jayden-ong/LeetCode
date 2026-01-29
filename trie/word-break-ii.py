class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        length_s = len(s)
        answer = []

        def recursive(curr_index, curr_sentence, curr_word):
            # Need to add space before adding word
            answer = []
            if curr_index >= length_s:
                # If curr_word is "", sentence is complete
                if curr_word == "":
                    return [curr_sentence]
                return []
            
            curr_word += s[curr_index]
            # If word is in word_set, we could add it to the sentence
            # We could also choose to skip adding the word
            answer += recursive(curr_index + 1, curr_sentence, curr_word)
            if curr_word in word_set:
                curr_sentence += " " + curr_word
                answer += recursive(curr_index + 1, curr_sentence, "")
            
            return answer


        for i in range(length_s):
            curr_seg = s[:i + 1]
            if curr_seg in word_set:
                answer.extend(recursive(i + 1, curr_seg, ""))
        return answer
