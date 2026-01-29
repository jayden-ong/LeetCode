class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        length_s = len(s)
        left = 0
        right = length_s - 1
        first_half = ""
        second_half = ""
        while left <= right:
            if left == right:
                first_half += s[left]
            elif s[left] == s[right]:
                first_half += s[left]
                second_half = s[right] + second_half
            else:
                first_half += min(s[left], s[right])
                second_half = min(s[left], s[right]) + second_half
                
            left += 1
            right -= 1
        return first_half + second_half