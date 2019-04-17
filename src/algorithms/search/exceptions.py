class NoElementFoundError(Exception):
    """Base class for other exceptions"""
    def __init__(self,number):
        Exception.__init__(self, "Element {0} not found".format(number))
