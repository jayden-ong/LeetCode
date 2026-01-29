class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        string_length = len(s)
        for i in range(string_length // 2):
            temp = s[i]
            s[i] = s[string_length - i - 1]
            s[string_length - i - 1] = temp
        