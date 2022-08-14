# Task 1 Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def below_arithm_mean(list):
    #finding arithmetical mean
    sum_of_elements = 0
    for n in list:
        sum_of_elements = sum_of_elements + n
    arithm_mean = sum_of_elements / len(list)
    print(f'The arithmetical mean is {arithm_mean}')
    # appending values below arithmetical mean to list_2
    list_2 = []
    for n in list:
        if n < arithm_mean:
            list_2.append(n)
    return list_2

list_1 = [1, 3, 5, 6, 4, 10, 2, 3]
print(below_arithm_mean(list_1))

#Task 2 Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def two_lowest_elements(list):
    list.sort()
    return list[0], list[1]

list_3 = [198, 3, 4, 9, 10, 9, 2]
print(two_lowest_elements(list_3))

