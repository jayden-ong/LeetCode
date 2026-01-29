class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        forward = True
        curr_time = 0
        while curr_time + n - 1 <= time:
            curr_time += n - 1
            forward = not forward
        if forward:
            return time - curr_time + 1
        return n - (time - curr_time)