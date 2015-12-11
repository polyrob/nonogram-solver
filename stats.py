import datetime
import time

__author__ = 'x789997'


class Stats:
    """ Solution Class """
    start_time = time.time()
    iteration = 0

    def __init__(self):
        print('Solution initialized at', datetime.datetime.now())

    def iterate(self):
        self.iteration += 1
        self.print_summary()

    def print_summary(self, completed=False):
        if completed: print("Processing Completed Successfully!")
        print('Iteration %d, Time elapsed (sec): %.3f' % (self.iteration, self.get_elapsed()))

    def get_elapsed(self):
        return time.time() - self.start_time
