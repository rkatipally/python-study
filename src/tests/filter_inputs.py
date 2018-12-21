from unittest import TestCase
from unittest.mock import patch


class FilterInputs:
    def filter_inputs(self, data):
        return [n for n in data if self.is_positive(n)]

    def is_positive(self, number):
        return number > 0


