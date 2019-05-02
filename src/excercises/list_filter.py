def filter_list(in_list, limit):
    out_list = []
    for n in in_list:
        if n < limit:
            out_list.append(n)
    return out_list


print("Please enter a limit number:")
limit_number = input()
list_to_be_filtered = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(filter_list(list_to_be_filtered, int(limit_number)))

