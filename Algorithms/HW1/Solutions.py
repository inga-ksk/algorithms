#1
def sum_of_digits(n):
    sum = 0
    for d in range(n+1):
        sum = sum + d
    return sum

print(sum_of_digits(12))

#2
def max_number(n):
    list = []
    for i in range(n):
        list.append(int(input("please enter a number: ")))
    max_number = list[0]
    for d in list:
        if d > max_number:
            max_number = d
    return max_number

print(max_number(3))

#3
def odd_even_counter():
    input_number = input("Please enter any whole number: ")
    odd_count = 0
    even_count = 0
    for digit in [int(i) for i in input_number]:
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"There are {even_count} even digits, {odd_count} odd digits in this number")

odd_even_counter()

