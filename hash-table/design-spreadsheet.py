class Spreadsheet:

    def __init__(self, rows: int):
        self.columns = {}
        for i in range(65, 91):
            self.columns[chr(i)] = [0] * rows

    def setCell(self, cell: str, value: int) -> None:
        column = cell[0]
        row = int(cell[1:])
        self.columns[column][row - 1] = value

    def resetCell(self, cell: str) -> None:
        column = cell[0]
        row = int(cell[1:])
        self.columns[column][row - 1] = 0

    def getValue(self, formula: str) -> int:
        val1, val2 = formula[1:].split("+")
        if 65 <= ord(val1[0]) <= 90:
            column = val1[0]
            row = int(val1[1:])
            final_val1 = self.columns[column][row - 1]
        else:
            final_val1 = int(val1)
        
        if 65 <= ord(val2[0]) <= 90:
            column = val2[0]
            row = int(val2[1:])
            final_val2 = self.columns[column][row - 1]
        else:
            final_val2 = int(val2)
        return final_val1 + final_val2
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)