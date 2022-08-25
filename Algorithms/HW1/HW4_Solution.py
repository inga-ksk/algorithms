# #1 Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(list):
    index = -1
    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            index += 1
            list[i], list[index] = list[index], list[i]
    return list

list_1 = [7, 3, 5, 6, 4, 10, 3, 2]
print(even_first(list_1))

#2 Write a program that takes as input a list of digits encoding a nonnegative decimal integer D
# and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def list_to_integer(list):
    integer = 0
    for i in list:
        integer *= 10
        integer += i
    result = integer + 1
    return result

list_1 = [1, 2, 9]
print(list_to_integer(list_1))






