from unittest import TestCase
from unittest.mock import patch, call

from src.tests.filter_inputs import FilterInputs


class FilterInputTest(TestCase):
    @patch('src.tests.filter_inputs.FilterInputs.is_positive')
    def test_filter_inputs(self, is_positive_mock):
        v = [3,-4,0,1]
        filterInputs = FilterInputs()
        filterInputs.filter_inputs(v)
        self.assertEqual([call(3), call(-4), call(0), call(1)], is_positive_mock.call_args_list)
