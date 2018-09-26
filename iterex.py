"""Example Iterator python code"""


class IterClass:
    """This is class IterClass"""

    def __init__(self, m):
        """This is Init function"""
        self.max = m
        self.num = 0

    def __iter__(self):
        """This is iter function"""
        #self.num = 0
        return self

    def __next__(self):
        """This is next function"""
        if self.num <= self.max:
            res = self.num
            self.num += 2
        else:
            raise StopIteration
        return res
