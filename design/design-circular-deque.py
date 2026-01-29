class MyCircularDeque:

    def __init__(self, k: int):
        self.curr_size = 0
        self.max_size = k
        self.queue = [None] * self.max_size
        self.front_pointer = 0
        self.back_pointer = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.queue[self.front_pointer] is not None:
            self.front_pointer -= 1
            if self.front_pointer < 0:
                self.front_pointer = self.max_size - 1
        
        self.queue[self.front_pointer] = value
        self.curr_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.queue[self.back_pointer] is not None:
            self.back_pointer = (self.back_pointer + 1) % self.max_size
        
        self.queue[self.back_pointer] = value
        self.curr_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.queue[self.front_pointer] = None
        self.curr_size -= 1
        if self.curr_size == 0:
            return True
        
        self.front_pointer = (self.front_pointer + 1) % self.max_size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.queue[self.back_pointer] = None
        self.curr_size -= 1
        if self.curr_size == 0:
            return True
        
        self.back_pointer -= 1
        if self.back_pointer < 0:
            self.back_pointer = self.max_size - 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front_pointer]
        
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.back_pointer]

    def isEmpty(self) -> bool:
        return self.curr_size == 0
        
    def isFull(self) -> bool:
        return self.curr_size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()