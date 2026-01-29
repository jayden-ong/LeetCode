class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.products = []
        self.most_recent_zero = -1
        self.multiplier = 1

    def add(self, num: int) -> None:
        self.nums.append(num)
        if (len(self.products) > 0 and self.products[-1] == 0) or len(self.products) == 0:
            self.products.append(num)
            self.multiplier = num
        else:
            self.products.append(num * self.products[-1])
            self.multiplier *= num
        
        if num == 0:
            self.most_recent_zero = len(self.nums) - 1
        
    def getProduct(self, k: int) -> int:
        if self.most_recent_zero >= 0 and len(self.nums) - k <= self.most_recent_zero:
            return 0
        
        if k == len(self.nums) or self.products[len(self.products) - k - 1] == 0:
            return self.multiplier
        return self.multiplier // self.products[len(self.products) - k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)