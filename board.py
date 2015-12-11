__author__ = 'x789997'

WHITE_0 = '0'
BLACK_1 = '1'

WHITE_PRINT = '░'
BLACK_PRINT = '█'


class Board:
    """ Board Class """
    rows = []

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

    def print(self):
        for row in self.rows:
            charrow = ""
            for cell in row:
                if cell == False:
                    charrow += WHITE_PRINT
                else:
                    charrow += BLACK_PRINT
            print(charrow)

    def get_row(self, index):
        return self.rows[index - 1]

    def get_col(self, index):
        arr = []
        for row in self.rows:
            arr.append(row[index - 1])
        return arr

    def set_black(self, row, col):
        self.rows[row - 1][col - 1] = True


if __name__ == '__main__':
    b = Board('starter_board.txt')
    # b.set_black(4,13)

    b.print()

    print('Row 4 is', b.get_row(4))
    print('Col 4 is', b.get_col(4))