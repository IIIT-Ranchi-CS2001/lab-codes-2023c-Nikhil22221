# 1. Define a function my_zip() that can form a list of tuples by iterating the following customer details:- ‘customer Name, customer ID , shopping points’ and based on the keyword parameter ‘strct’:
# If strct = True, zipping shall be done only if all lists are of equal length. 
# If strct = False, zipping can be done by taking the minimum length of the iterable.
def custom_zip(names, ids, points, strict):
    if strict:
        if len(names) == len(ids) == len(points):
            return list(zip(names, ids, points))
        else:
            return "Lengths of the lists are not equal"
    else:
        return list(zip(names, ids, points))

names_list = [name for name in input("Enter customer names: ").split()]
ids_list = [int(identifier) for identifier in input("Enter customer ids: ").split()]
points_list = [int(points) for points in input("Enter shopping points: ").split()]
is_strict = bool(input("Enter True or False: "))
zipped_list = custom_zip(names_list, ids_list, points_list, is_strict)

print(zipped_list)

# Define a function my_sort() to sort the list of tuples created using my_zipfunction in the last question. 
# The function must have two types of arguments- the list that carry the data, the key that determines the argument of sorting
# Key = 0: sorting based on customer name in ascending order
# Key = 1: sorting based on Customer ID
# Key = 2: sorting based on shopping points
def custom_sort(zipped, sort_key):
    if sort_key == 0:
        zipped.sort(key=lambda x: x[0])
    elif sort_key == 1:
        zipped.sort(key=lambda x: x[1])
    elif sort_key == 2:
        zipped.sort(key=lambda x: x[2])

sort_key = int(input("Enter the key: "))
custom_sort(zipped_list, sort_key)
print(zipped_list)

# 3. Write program to define a function my_max() to complete the following tasks: [Usage of built-in function max() is strictly prohibited]
# If a list of integers is passed as the input argument, the function shall return maximum value present in the list
# If a set is passed, maximum value present in the list
# If a tuple is passed, maximum value present in the tuple
# Hint: Pass the container type unpacked using *

def my_max(args):
    m=0
    for i in args:
        if i>m:
            m=i
    return m

myset = { int(x) for x in input("Enter the numbers: ").split()}
max_number = my_max(myset)
print(max_number)

# 4. Write a python script using map, lambda and filter functions to do the following operations on a user inputted comma separated strings: E.g.: “Tom 25 Rahu22 2@$” 
# To find all the letters given in the string and to convert them to uppercase
# o/p: [‘TOM’]
# To find all the digits present in the string and to find their squares
# o/p: [625]
# To display all the alphanumeric characters present in the string
# o/p: [“Tom”, ‘25’, “Rahu22”]

input_string = input("Enter the string: ")

def to_uppercase(string):
    return string.upper()

upper_string = to_uppercase(input_string)
print(upper_string)

def square_numbers(string):
    numbers = [int(num) for num in string.split() if num.isdigit()]
    return [num ** 2 for num in numbers]

squared_list = square_numbers(input_string)
print(squared_list)

def find_alphanumeric_words(string):
    return [word for word in string.split() if word.isalnum()]

alphanumeric_list = find_alphanumeric_words(input_string)
print(alphanumeric_list)

