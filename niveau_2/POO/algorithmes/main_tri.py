import random


def random_list_generator(n, min, max):
    list = []
    for i in range(0, n):
        list.append(random.randint(min, max))
    return list


def tri_par_selection(list):
    for unsorted_index in range(0, len(list)-1):
        min = list[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1, len(list)):
            if min > list[i]:
                min = list[i]
                min_index = i
        list[min_index]=list[unsorted_index]
        list[unsorted_index] = min
    return list

test_list = random_list_generator(10,0,10)
print(test_list)
print(tri_par_selection(test_list))