def sort(list_to_sort):
    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort)):
            if list_to_sort[i] < list_to_sort[j]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[j]
                list_to_sort[j] = temp
    return list_to_sort


list_to_sort = [2,4,1,6,4,3]
sort(list_to_sort)
print(list_to_sort)
