class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # If there is a palindrome that starts with the first letter of the string,
        # we only have to copy the letters after that palindrome, reverse them, then
        # add it to the beginning of the string to get a palindrome. 

        # Brute force : reverse the string, keep adding letters from end to front
        # until string is a palindrome.
        reverse_s = s[::-1]
        curr = ""
        if s == s[::-1]:
            return s
        
        for letter in reverse_s:
            curr += letter
            answer = curr + s
            if answer == answer[::-1]:
                return answer
        # Should never reach here
        return ""