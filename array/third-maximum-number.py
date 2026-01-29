class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = None
        second_max = None
        third_max = None
        for num in nums:
            if first_max is None:
                first_max = num
            elif second_max is None:
                if num < first_max:
                    second_max = num
                elif num != first_max:
                    second_max = first_max
                    first_max = num
            elif third_max is None:
                if num < second_max:
                    third_max = num
                elif num > second_max and num < first_max:
                    third_max = second_max
                    second_max = num
                elif num > first_max:
                    temp1 = first_max
                    first_max = num
                    third_max = second_max
                    second_max = temp1
            else:
                if num > first_max:
                    temp1 = first_max
                    first_max = num
                    third_max = second_max
                    second_max = temp1
                elif num < first_max and num > second_max:
                    third_max = second_max
                    second_max = num
                elif num < second_max and num > third_max:
                    third_max = num
            
        if third_max is None:
            return first_max
        return third_max