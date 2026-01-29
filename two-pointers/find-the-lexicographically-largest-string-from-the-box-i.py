class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        # The longest string is len(word) - numFriends + 1
        max_length = len(word) - numFriends + 1
        answer = word[:min(len(word), max_length)]
        for i in range(1, len(word)):
            answer = max(answer, word[i:min(len(word), i + max_length)])
        return answer