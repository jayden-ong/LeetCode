class Robot:

    def __init__(self, width: int, height: int):
        self.top_right = (height, width)
        self.pos = [0, 0]
        self.dir = "East"

    def step(self, num: int) -> None:
        rotation_direction = {"North" : "West", "East" : "North", "South" : "East", "West" : "South"}
        direction_to_step = {"North" : (1, 0), "East" : (0, 1), "South" : (-1, 0), "West" : (0, -1)}
        while num > 0:
            new_row, new_col = self.pos[0] + direction_to_step[self.dir][0], self.pos[1] + direction_to_step[self.dir][1]
            if 0 <= new_row < self.top_right[0] and 0 <= new_col < self.top_right[1]:
                self.pos = [new_row, new_col]
                num -= 1
            else:
                self.dir = rotation_direction[self.dir]

    def getPos(self) -> List[int]:
        return [self.pos[1], self.pos[0]]

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()