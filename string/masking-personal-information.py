class Solution:
    def maskPII(self, s: str) -> str:
        # Phone numbers cannot have "@"
        if '@' in s:
            name, domain = s.split('@')
            new_email = ""
            for i in range(len(name)):
                if i == 0:
                    new_email += name[i].lower()
                elif i == len(name) - 1:
                    new_email += "*****" + name[i].lower()
                
            new_email += "@"
            for char in domain:
                new_email += char.lower()
            return new_email
        
        numbers = ""
        for char in s:
            if char in '0123456789':
                numbers += char
        
        # No matter what the last four digits are always the same
        if len(numbers) == 10:
            return "***-***-" + numbers[6:]
        elif len(numbers) == 11:
            return "+*-***-***-" + numbers[7:]
        elif len(numbers) == 12:
            return "+**-***-***-" + numbers[8:]
        return "+***-***-***-" + numbers[9:]