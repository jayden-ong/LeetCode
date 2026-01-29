class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def convert_to_string(first, second, third):
            return str(first) + str(second) + str(third)
        
        nums_added = set()
        digits.sort()
        num_digits = len(digits)
        answer = []
        for i in range(num_digits):
            if digits[i] != 0:
                for j in range(num_digits):
                    if i != j:
                        for k in range(num_digits):
                            if i != k and j != k:
                                num_to_consider = int(convert_to_string(digits[i], digits[j], digits[k]))
                                if digits[k] % 2 == 0 and num_to_consider not in nums_added:
                                    answer.append(num_to_consider)
                                    nums_added.add(num_to_consider)
        return answer