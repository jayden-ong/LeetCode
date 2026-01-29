class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_filter = filter(lambda x:x.isalnum(), s)
        new_string = "".join(string_filter).lower()
        return new_string == new_string[::-1]