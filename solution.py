import datetime
import time

__author__ = 'x789997'


class Solution:
    """ Solution Class """
    start_time = time.time()
    iteration = 0

    def __init__(self):
        print('Solution initialized at', datetime.datetime.now())

    def print_summary(self):
        print('Iteration %d, Time elapsed (sec): %.3f' % (self.iteration, self.get_elapsed()))

    def get_elapsed(self):
        return time.time() - self.start_time
