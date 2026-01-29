class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev_say = self.countAndSay(n - 1)
            curr_ans = []
            curr_char = prev_say[0]
            curr_streak = 1
            length_prev = len(prev_say)
            for i in range(1, len(prev_say)):
                if prev_say[i] == curr_char:
                    curr_streak += 1
                else:
                    curr_ans.append(str(curr_streak) + curr_char)
                    curr_char = prev_say[i]
                    curr_streak = 1
            curr_ans.append(str(curr_streak) + curr_char)
            return ''.join(curr_ans)