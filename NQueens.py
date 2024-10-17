#Class for representing NQueens problem
import numpy as np

class NQueens:

    def __init__(self, n):
        self.queens = np.random.randint(n, size=n)
        self.n = n

    def getQueens(self):
        return self.queens

    def getN(self):
        return self.n
