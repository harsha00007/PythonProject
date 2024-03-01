my_list = [3, 2, 1, 8, 4, 5, 6]
"""Append an element to the list."""
my_list.append(7)
print(my_list)

"""Remove an element from the list."""
my_list.remove(3)
print(my_list)

"""Sort the list in ascending order."""
my_list.sort()
print(my_list)

"""Reverse the list."""
print(my_list[::-1])

"""List comprehension"""
list_comp = [i for i in range(10)]
print(list_comp)

"""Create a program that generates a list of squares of numbers from 1 to 10 using list comprehension."""
square_list = [i * i for i in range(11)]
print(square_list)

"""Write a program to merge two lists into a single list."""
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 0]
list3 = list1 + list2
print(list3)

"""Create a program that demonstrates various operations on tuples like accessing elements, slicing,"""
my_tup = (1, 3, 4, 5, 6, 7, 8, 9)
print(my_tup[4])
print(my_tup[2: 5])

"""concatenating tuples."""
tup1 = (1, 3, 4, 5, 7, 8)
tup2 = (3, 4, 5, 2, 6, 0)
tup3 = tup1 + tup2
print(tup3)

"""Write a function that takes a tuple as input and returns the sum of its elements."""
user_input = (1, 2, 3, 5, 6, 7, 8)
total = sum(user_input)
print(total)

"""Write a program that sorts a list of tuples based on the second element of each tuple."""
my_list = [(33, 5), (6, 7), (9, 3), (7, 9)]
sort_list = sorted(my_list, key=lambda x: x[1])
print(sort_list)

"""Create a program that demonstrates basic dictionary operations like adding a key-value pair, removing a key,
and accessing values using keys."""
my_dict = {"name": "harsha", "age": 21}
my_dict.update({"place": "shivamoga"})
print(my_dict)
my_dict.pop("name")
print(my_dict)
print(my_dict["age"])

"""Write a program that generates a dictionary where keys are numbers from 1 to 5, and values are the squares of the
keys."""
dict_comp = {i: i * i for i in range(1, 6)}
print(dict_comp)

"""Write a program to sort a dictionary by its values in ascending order."""
my_dict = {1: 94, 2: 61, 4: 87, 5: 98, 6: 33, 7: 77}
for i, j in my_dict.items():
    pass

"""Write a program that merges two dictionaries into one."""
dict1 = {1: 34, 2: 45, 3: 76, 4: 78}
dict2 = {"name": "a", "place": "bglr", "course": "python"}
dict1.update(dict2)
print(dict1)

"""Prompt the user to enter two numbers and perform division. Handle the ZeroDivisionError exception gracefully by
displaying a meaningful error message."""
try:
    a = 5
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

"""Prompt the user to enter an integer. Use exception handling to handle the ValueError if the input is not an 
integer. Display an appropriate message to the user."""
try:
    user_input = int(input("enter number: "))
except ValueError:
    print("value error")
else:
    print(user_input)

"""Attempt to open a file (you can choose the file name). Handle the FileNotFoundError exception if the file does not 
exist. Display a message indicating the issue."""

try:
    with open("harsha.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")

"""Define a custom exception called CustomError. Raise this exception in a specific scenario within your program (
e.g., if a certain condition is not met). Handle this custom exception and display a customized error message."""
