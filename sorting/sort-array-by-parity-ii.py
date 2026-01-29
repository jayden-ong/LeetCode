class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        num_even = 0
        num_odd = 0
        for num in nums:
            if num % 2 == 0:
                num_even += 1
                even.append(num)
            else:
                num_odd += 1
                odd.append(num)
        odd_pointer = 0
        even_pointer = 0
        answer = []
        while even_pointer < num_even and odd_pointer < num_odd:
            answer.append(even[even_pointer])
            answer.append(odd[odd_pointer])
            even_pointer += 1
            odd_pointer += 1
        return answer