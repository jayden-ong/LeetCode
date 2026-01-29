class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {0 : "",
                      4 : "IV",
                      9 : "IX",
                      40 : "XL",
                      90 : "XC",
                      400 : "CD",
                      900 : "CM"
        }
        if num in roman_dict:
            return roman_dict[num]
        # 1-3
        if num <= 3:
            return "I" * num
        # 5-8
        elif num <= 8:
            # Could replace recursive call with (num % 5) * "I"
            return "V" + self.intToRoman(num % 5)
        # 10 - 39
        elif num <= 39:
            return ("X" * (num // 10)) + self.intToRoman(num % 10)
        # 41 - 49
        elif num <= 49:
            return "XL" + self.intToRoman(num % 40)
        # 50 - 89
        elif num <= 89:
            return "L" + self.intToRoman(num % 50)
        # 91 - 99
        elif num <= 99:
            return "XC" + self.intToRoman(num % 90)
        # 101 - 399
        elif num <= 399:
            return ("C" * (num // 100)) + self.intToRoman(num % 100)
        # 401 - 499
        elif num <= 499:
            return "CD" + self.intToRoman(num % 400)
        # 501 - 899
        elif num <= 899:
            return "D" + self.intToRoman(num % 500)
        # 900 - 999
        elif num <= 999:
            return "CM" + self.intToRoman(num % 900)
        # 1000+
        else:
            return ("M" * (num // 1000)) + self.intToRoman(num % 1000)