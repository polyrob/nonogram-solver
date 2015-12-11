from board import Board
from data import Data
from solution import Solution

__author__ = 'x789997'



def partition(plist, n, k, b):
    """ Get the distributions of the ways n can be spread across k buckets """
    if k == 1:
        plist.append(b + [n])
        return

    for i in range(n + 1):
        partition(plist, n - i, k - 1, b + [i])


def getPartitions():
    grouplist = []
    partition(grouplist, 8, 5, [])
    return grouplist





if __name__ == '__main__':
    s = Solution()
    b = Board('starter_board.txt')
    d = Data("rowdata.txt", "coldata.txt")

    s.print_summary()