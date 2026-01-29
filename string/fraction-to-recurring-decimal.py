class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        answer = ""
        # One is negative
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            answer += "-"
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        answer += str(numerator // denominator)
        remainder = numerator % denominator
        # Answer is whole number
        if remainder == 0:
            return answer
        
        answer += "."
        remainder_to_length_dict = {}
        # Need to figure out where to add a bracket -- if there is a repeating remainder
        while remainder != 0:
            if remainder in remainder_to_length_dict:
                answer = answer[:remainder_to_length_dict[remainder]] + "(" + answer[remainder_to_length_dict[remainder]:] + ")"
                break
            remainder_to_length_dict[remainder] = len(answer)
            remainder *= 10
            answer += str(remainder // denominator)
            remainder %= denominator
        return answer

