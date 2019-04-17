from datetime import datetime

from src.algorithms.search.exceptions import NoElementFoundError


def linear_search(list_of_numbers, element_to_find):
    for position, num in enumerate(list_of_numbers):
        if num == element_to_find:
            return position
    raise NoElementFoundError(element_to_find)


startTime = datetime.now()
list_of_numbers = [1,2,1,2,1,2,33,4,5,31,2,3,4,5,4,53,4,5]
element_to_find = 54
position = -1
try:
    position = linear_search(list_of_numbers, element_to_find)
except NoElementFoundError as error:
    print("Exception occurred: {}".format(error.args[0]))


print("Element {0} found at {1}".format(element_to_find, position))
print("Total time to search {0}".format(datetime.now() - startTime))
