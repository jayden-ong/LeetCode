class RecentCounter:

    def __init__(self):
        self.requests = []
        self.num_requests = 0
        self.curr_index = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.num_requests += 1
        for i in range(self.curr_index, self.num_requests):
            if self.requests[i] >= t - 3000:
                self.curr_index = i
                return self.num_requests - i
        return 0


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)