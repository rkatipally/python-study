import math 
from functools import reduce
import string


class FunctionsFun():
    def __init__(self):
        print('Initializing FunctionsFun!!')

    @staticmethod
    def call_me(method_name, input):
        print(method_name.center(100, '='))
        method = getattr(FunctionsFun, method_name)
        try:
            iter(input)
            output = method(*input)
        except TypeError:
            output = method(input)
        print(f'Input: {input}\nOutput: {output}')

    @staticmethod
    def calc_sphere_volume(radius):
        return round((4 * math.pi * radius ** 3) / 3, 2)

    @staticmethod
    def range_check(num, low, high):
        return low <= num <= high

    @staticmethod
    def up_low(s):
        lower_count = 0
        upper_count = 0
        for char in list(s):
            if char.islower():
                lower_count += 1
            if char.isupper():
                upper_count += 1
        return lower_count, upper_count

    @staticmethod
    def unique_list(l):
        return sorted(set(l))

    @staticmethod
    def multiply(l):
        return reduce((lambda x, y: x * y), l)

    @staticmethod
    def palindrome(s):
        return s == s[::-1]

    @staticmethod
    def is_pangram(s):
        return set(s.lower()) >= set(string.ascii_lowercase)


FunctionsFun.call_me('calc_sphere_volume', 10)
FunctionsFun.call_me('range_check', (5, 2, 7))
FunctionsFun.call_me('up_low', "Hello Mr. Rogers, how are you this fine Tuesday?")
FunctionsFun.call_me('unique_list', [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
FunctionsFun.call_me('multiply', [1, 2, 3, 5, 6])
FunctionsFun.call_me('palindrome', 'ABCBA')
FunctionsFun.call_me('is_pangram', 'The quick brown fox jumps over the lazy dog')
