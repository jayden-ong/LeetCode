class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr_prefix = ""
        curr_word = strs[0]
        for i in range(0, len(curr_word)):
            curr_letter = curr_word[i]
            for j in range(0, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != curr_letter:
                    return curr_prefix
            curr_prefix += curr_letter
        
        return curr_prefix