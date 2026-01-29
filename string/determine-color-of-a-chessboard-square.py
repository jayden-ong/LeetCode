class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in 'aceg' and coordinates[1] in "2468":
            return True
        elif coordinates[0] in 'bdfh' and coordinates[1] in "1357":
            return True
        return False