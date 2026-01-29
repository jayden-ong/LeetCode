class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        answer = ""
        for word in dictionary:
            curr_index = 0
            for letter in s:
                if letter == word[curr_index]:
                    curr_index += 1
                
                if curr_index == len(word):
                    if len(word) > len(answer) or (len(word) == len(answer) and word < answer):
                        answer = word
                    break
        return answer