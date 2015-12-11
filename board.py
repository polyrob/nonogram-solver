__author__ = 'x789997'

WHITE_0 = '0'
BLACK_1 = '1'

WHITE_PRINT = '░'
BLACK_PRINT = '█'


class Board:
    """ Board Class """
    rows = []
    cols = []

    possiblerows = []
    possiblecols = []

    solvedrows = []
    solvedcols = []

    def __init__(self, filename):
        with open(filename, "r") as ins:
            for line in ins:
                linearray = []
                for char in line:
                    if char == WHITE_0:
                        linearray.append(False)
                    elif char == BLACK_1:
                        linearray.append(True)
                self.rows.append(linearray)
        for rowindex, row in enumerate(self.rows):
            column = []
            for colindex in range(25):
                column.append(self.rows[colindex][rowindex])
            self.cols.append(column)



    def print(self):
        for row in self.rows:
            charrow = ""
            for cell in row:
                if not cell:
                    charrow += WHITE_PRINT
                else:
                    charrow += BLACK_PRINT
            print(charrow)

    def set_black(self, row, col):
        self.rows[row - 1][col - 1] = True

    def is_solved(self, series, totalblk):
        pass




if __name__ == '__main__':
    b = Board('starter_board.txt')
    # b.set_black(4,13)
    b.print()
