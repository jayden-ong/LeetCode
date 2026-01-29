class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = [(1, 0)]
        def check_valid(word1, word2):
            if len(word1) != len(word2):
                return False
            
            difference = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    difference += 1
                    if difference > 1:
                        return False
            return True

        answer_index = 0
        for i in range(1, len(words)):
            curr_answer = 1
            curr_index = i
            for j in range(i):
                if check_valid(words[i], words[j]) and groups[i] != groups[j]:
                    if dp[j][0] + 1 > curr_answer:
                        curr_answer = dp[j][0] + 1
                        curr_index = j
            
            dp.append((curr_answer, curr_index))
            if dp[answer_index][0] < dp[i][0]:
                answer_index = i
            
        answer = []
        curr_index = answer_index
        while curr_index != dp[curr_index][1]:
            answer.append(words[curr_index])
            curr_index = dp[curr_index][1]
        answer.append(words[curr_index])
        return answer[::-1]