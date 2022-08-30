#1 Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.

def selection_sort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1, len(list)-1):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return(list)

list1 = [5, 6, 34, 2, 12, 456]
print(selection_sort(list1))

#2 Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

def bubble_sort(new_list):
    for i in range(len(new_list)):
        for j in range(len(new_list) - 1):
            if new_list[j] > new_list[j+1]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    return new_list

list2 = [555, 34, 890, 200, 120000, 4578786]
print(bubble_sort(list2))
#
# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.

def insertion_sort(input_list):
    for index in range(1, len(input_list)):
        current_value = input_list[index]
        current_position = index
        while current_position > 0 and input_list[current_position - 1] > current_value:
            input_list[current_position] = input_list[current_position -1]
            current_position = current_position - 1
        input_list[current_position] = current_value
    return input_list

list3 = [6767, 364, 8909889, 20, -8, 786]
print(insertion_sort(list3))
#
# Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    first = merge_sort(arr[:middle])
    second = merge_sort(arr[middle:])
    return merge_arrays(first, second)

def merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j+=1
            continue
        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i+=1
            continue

        if left_arr[i] <= right_arr[j]:
            merged_array.append(left_arr[i])
            i+=1
        else:
            merged_array.append(right_arr[j])
            j+=1
    return merged_array

list4 = [677, 367874, 9, -20, -8, 89786]
print(merge_sort(list4))