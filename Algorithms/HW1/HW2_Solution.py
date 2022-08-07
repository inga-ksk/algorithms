# 1. Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_in_half():
    string_1 = input('Please enter any string: ')
    if len(string_1) % 2 == 0:
        i = int(len(string_1)/2)
    else:
        i = int((len(string_1)/2) + 1)
    new_string = (string_1[(i)::]) + (string_1[:i])
    return new_string

print(split_in_half())

# 2. Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
# Hint: https://www.w3schools.com/python/python_sets.asp

def find_unique_chars():
    string_2 = input("Please enter any string: ")
    #convert string to set with unique letters
    unique_chars = set(string_2)
    if len(string_2) == len(unique_chars):
        return True
    else:
        return False

print(find_unique_chars())
