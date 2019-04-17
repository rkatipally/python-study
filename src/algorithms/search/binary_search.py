from datetime import datetime

from src.algorithms.search.exceptions import NoElementFoundError


def binary_search_nr(sorted_list, element_to_search):
    start = 0
    end = len(sorted_list)-1
    while start < end:
        mid = (start + end)//2
        if sorted_list[mid] == element_to_search:
            return mid
        elif sorted_list[mid] > element_to_search:
            end = mid - 1
        else:
            start = mid + 1

    raise NoElementFoundError(element_to_search)


def binary_search_recursive(sorted_list, element_to_search, start, end):
    if start > end:
        raise NoElementFoundError(element_to_search)
    else:
        mid = (start + end)//2
        if sorted_list[mid] == element_to_search:
            return mid
        elif sorted_list[mid] > element_to_search:
            return binary_search_recursive(sorted_list, element_to_search, start, mid - 1)
        else:
            return binary_search_recursive(sorted_list, element_to_search, mid + 1, end)


sorted_list = [1,3,6,8,12,24,56,67]
element_to_search = 564

try:
    startTime = datetime.now()
    found_index = binary_search_recursive(sorted_list, element_to_search, 0, len(sorted_list)-1)
    print("Using Recursive binary search:: Element {0} is found at {1} in {2} time".format(element_to_search, found_index, (datetime.now() - startTime)))
except NoElementFoundError as ne:
    print(ne)

finally:
    print("Completed the Recursive search")


try:
    startTime = datetime.now()
    found_index = binary_search_nr(sorted_list, element_to_search)
    print("Using Non-recursive binary search:: Element {0} is found at {1} in {2} time".format(element_to_search, found_index, (datetime.now() - startTime)))
except NoElementFoundError as ne:
    print(ne)

finally:
    print("Completed the Non-recursive search")


