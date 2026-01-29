class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        has_lowercase = False
        has_uppercase = False
        has_digit = False
        has_special = False
        prev = None
        pass_length = 0
        for char in password:
            if char.islower():
                has_lowercase = True
            
            if char.isupper():
                has_uppercase = True

            if char.isnumeric():
                has_digit = True

            if char in "!@#$%^&*()-+":
                has_special = True
            
            if prev == char:
                return False
            prev = char
            pass_length += 1
        return has_lowercase and has_uppercase and has_digit and has_special and pass_length >= 8
