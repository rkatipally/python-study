from unittest import TestCase
from unittest.mock import patch, call

from src.tests.filter_inputs import FilterInputs


class FilterInputTest(TestCase):
    @patch('src.tests.filter_inputs.FilterInputs.is_positive')
    def test_filter_inputs(self, is_positive_mock):
        v = [3, -4, 0, 1]
        filter_nputs = FilterInputs()
        filter_nputs.filter_inputs(v)
        self.assertEqual([call(3), call(-4), call(0), call(1)], is_positive_mock.call_args_list)

    @patch('src.tests.filter_inputs.FilterInputs')
    def test_filter_inputs(self, filter_inputs_mock):
        v = [3, -4, 0, 1]
        filter_inputs = filter_inputs_mock()
        filter_inputs.is_positive.return_value = True
        filter_inputs.filter_inputs.return_value = v
        result = filter_inputs.filter_inputs(v)
        self.assertEqual(result, v)

    @patch('src.tests.filter_inputs.FilterInputs.is_positive', return_value=False)
    def test_filter_inputs(self, is_positive_mock):
        v = [3, -4, 0, 1]
        filter_nputs = FilterInputs()
        result = filter_nputs.filter_inputs(v)
        self.assertEqual(result, [])
