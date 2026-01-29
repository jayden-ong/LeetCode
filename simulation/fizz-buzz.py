class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        curr_ans = [""] * n
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                curr_ans[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                curr_ans[i - 1] = "Fizz"
            elif i % 5 == 0:
                curr_ans[i - 1] = "Buzz"
            else:
                curr_ans[i - 1] = str(i)
        return curr_ans