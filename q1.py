list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_set = set1.intersection(set2)
    common_list = list(common_set)
    return common_list

common_list = common_elements(list1, list2)
print(common_list)
