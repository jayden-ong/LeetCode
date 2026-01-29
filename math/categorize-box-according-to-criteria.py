class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = False
        if length >= pow(10, 4) or width >= pow(10, 4) or height >= pow(10, 4) or length * width * height >= pow(10, 9):
            is_bulky = True
        
        is_heavy = False
        if mass >= 100:
            is_heavy = True
        
        if is_bulky and is_heavy:
            return "Both"
        elif is_bulky and not is_heavy:
            return "Bulky"
        elif not is_bulky and is_heavy:
            return "Heavy"
        return "Neither"
        
