from board import Board
from data import Data
from stats import Stats

__author__ = 'x789997'
s = Stats()


def partition(plist, n, k, b):
    """ Get the distributions of the ways n can be spread across k buckets """
    if k == 1:
        plist.append(b + [n])
        return

    for i in range(n + 1):
        partition(plist, n - i, k - 1, b + [i])


def getPartitions(size, buckets):
    grouplist = []
    partition(grouplist, size, buckets, [])
    return grouplist


def generate_possibles_from_spaces(rule, spaceplacement):
    possibles = []
    for spaces in spaceplacement:
        possible = []
        for index, val in enumerate(rule):
            for wht in range(spaces[index]):
                possible.append(False)
            for blk in range(val):
                possible.append(True)
            possible.append(False)
        # remove last white space
        possible.pop()
        # add last white, if it has it
        for wht in range(spaces[-1]):
            possible.append(False)

        possibles.append(possible)

    return possibles


def generate_all_possible(b, d):
    # generate rows
    allpossibles = []
    for index, row in enumerate(b.rows):
        rule = d.get_row_rules()[index]
        spacebuckets = len(rule) + 1
        totalspaces = 25 - sum(rule)
        playspaces = totalspaces - (len(rule) - 1)
        spaceplacement = getPartitions(playspaces, spacebuckets)
        allpossibles.append(generate_possibles_from_spaces(rule, spaceplacement))
        # generate columns
        pass




if __name__ == '__main__':
    # initialize objects
    d = Data("rowdata.txt", "coldata.txt")
    b = Board('starter_board.txt')

    # create lists of all possible configurations for rows/columns
    generate_all_possible(b, d)

    # start game loop
    solved = False
    # while not solved:
    #     s.iterate()
    # process(b, d.get_row_rules())


    # complete
    s.print_summary()
