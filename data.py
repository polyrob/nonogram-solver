__author__ = 'x789997'


class Data:
    """ Board Class """
    row_rules = []
    col_rules = []

    def __init__(self, rowfile, colfile):
        self.row_rules = self.get_rules_from_file(rowfile)
        self.col_rules = self.get_rules_from_file(colfile)


    def get_rules_from_file(self, filename):
        rules_list = []
        with open(filename, "r") as ins:
            for line in ins:
                linearray = []
                for val in line:
                    if val == '\n':
                        continue
                    elif val == 'a':
                        linearray.append(10)
                    else:
                        linearray.append(int(val))
                rules_list.append(linearray)
        return rules_list


if __name__ == '__main__':
    d = Data("rowdata.txt", "coldata.txt")
    print(d)
