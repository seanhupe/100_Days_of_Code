## Creating a New List from an existing List
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# ====================================================================================

## LIST COMPREHENSION - - works with Python Sequences: List, Range, String, Tuple
## formula for creating a new list from an existing
#new_list2 = [new_item for item in list]

# numbers2 = [4, 5, 6]
# new_list_add_one = [n + 1 for n in numbers2]
# print(new_list_add_one)

## This will separate and print each letter in a List
# name = "Sean"
# new_name = [letter for letter in name]
# print(new_name)

## Take range(a sequence we can iterate through), and create a range between 1 and 5
## Loop through and create a list where each # in range is doubled:  2, 4, 6, 8
##range_list(1, 5)
## Formula - xxxx = [new_item for item in list]
range_list = [num * 2 for num in range(1, 5)]
print(range_list)

# ====================================================================================

## CONDITIONAL LIST COMPREHENSION
## formula:   new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

## Create a new list of short names - - (less than 5 characters)
#short_names = [new_item for item in list if test]

short_names = [name for name in names if len(name) < 5]
print(short_names)

## Challenge - take above "names" list, and capitalize names that have more than 5 letters
##   answer will be CAROLINE, ELEANOR, FREDDIE
long_names = [n.upper() for n in names if len(n) > 5]
print(long_names)

# ====================================================================================

## CHALLENGES
#
# Squaring Numbers
# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.

#[new_item for item in list]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)


## Convert list of strings to integers
## Then create a new list of only even numbers

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# xxx = [new_item for item in list if test]
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)