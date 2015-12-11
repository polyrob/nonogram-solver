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


def determine_possibles(rules):
    possibles = []
    for index in range(25):
        rule = d.get_row_rules()[index]
        spacebuckets = len(rule) + 1
        totalspaces = 25 - sum(rule)
        playspaces = totalspaces - (len(rule) - 1)
        spaceplacement = getPartitions(playspaces, spacebuckets)
        possibles.append(generate_possibles_from_spaces(rule, spaceplacement))
    return possibles


def generate_all_possible(b, d):
    # generate rows/columns
    b.possiblerows = determine_possibles(d.get_row_rules())
    b.possiblecols = determine_possibles(d.get_col_rules())


def filter_possibles(b):
    total_probs_filtered = 0

    # work rows
    for rowindex, row in enumerate(b.rows):
        # if we know there is only one possible for this row now, skip
        if len(b.possiblerows[rowindex]) == 1: continue
        for cellindex, cell in enumerate(row):
            if cell:
                probs = len(b.possiblerows[rowindex])
                b.possiblerows[rowindex] = [prows for prows in b.possiblerows[rowindex] if prows[cellindex] is True]
                total_probs_filtered += (probs - len(b.possiblerows[rowindex]))

    # work columns
    for colindex, col in enumerate(b.cols):
        # if we know there is only one possible for this row now, skip
        if len(b.possiblecols[colindex]) == 1: continue
        for cellindex, cell in enumerate(col):
            if cell:
                probs = len(b.possiblecols[colindex])
                b.possiblecols[colindex] = [pcols for pcols in b.possiblecols[colindex] if pcols[cellindex] is True]
                total_probs_filtered += (probs - len(b.possiblecols[colindex]))

    print('Total possible rows filtered out this iterations: %d' % total_probs_filtered)


def apply_certainties(b):
    total_certainties_applied = 0

    # work rows
    for rowindex, row in enumerate(b.rows):
        if rowindex in b.solvedrows: continue
        for cellindex, cell in enumerate(row):
            # don't need to process if we've already set that cell black
            if cell is True: continue
            prows = b.possiblerows[rowindex]
            if all_true(prows, cellindex):
                b.rows[rowindex][cellindex] = True
                b.cols[cellindex][rowindex] = True
                total_certainties_applied += 1

    # work cols
    for colindex, col in enumerate(b.cols):
        if colindex in b.solvedcols: continue
        for cellindex, cell in enumerate(col):
            # don't need to process if we've already set that cell black
            if cell is True: continue
            pcols = b.possiblecols[colindex]
            if all_true(pcols, cellindex):
                b.cols[colindex][cellindex] = True
                b.rows[cellindex][colindex] = True
                total_certainties_applied += 1

    print('Total certainties applied: %d' % total_certainties_applied)
    return total_certainties_applied


def all_true(inputlist, index):
    for item in inputlist:
        if item[index] is False: return False
    return True


if __name__ == '__main__':
    # initialize objects
    d = Data("rowdata.txt", "coldata.txt")
    b = Board('starter_board.txt')

    # create lists of all possible configurations for rows/columns
    generate_all_possible(b, d)
    print('Generated all possibles from rules in %.3f sec' % s.get_elapsed())

    # start game loop
    solved = False
    while not solved:
        b.print()
        s.iterate()
        filter_possibles(b)
        solved_this_round = apply_certainties(b)

        # apply_knowns(b)




    # complete
    print('===== SUCCESS!! =====')
    b.print()
    s.print_summary()
