class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]
        
    def addCar(self, carType: int) -> bool:
        desired_space = carType - 1
        if self.spaces[desired_space] > 0:
            self.spaces[desired_space] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)