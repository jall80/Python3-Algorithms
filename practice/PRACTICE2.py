import json
import statistics
import random


print(" \n============== Create a list of five fruits. ==============\n ")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("The fruits lists is : {}".format(fruits))

print(" \n============== Modify elements ==============\n ")
# Change 'elderberry' to 'blueberry' in the list

for n in range(0, len(fruits)):
    if fruits[n] == "elderberry":
        fruits[n] = "blueberry"

print("The fruits lists is : {}".format(fruits))


print(" \n============== Check if an element exists ==============\n ")

def find_element(list_: list, element_to_search: str) -> bool:
    for element in list_:
        if element == element_to_search:
            return True
    else:
        return False


element_1 =  "banana"
element_2 = "peach"

print("The element \"{}\" is in the list: {}: {}.".format(element_1, fruits, find_element(fruits, element_1)))
print("The element \"{}\" is in the list: {}: {}.".format(element_2, fruits, find_element(fruits, element_2)))

print(" \n============== Reverse a list ==============\n ")

reversed_list =  fruits[::-1]

print("The reserved list of {} is : {}".format(fruits, reversed_list))

def complicate_func_to_reserve(list_ : list, step: int) -> list:

    list_copy = list_.copy()
    for n in range(0, int(len((list_copy))/2), step):
        list_copy[n], list_copy[-1-n]  = list_copy[-1-n], list_[n]
    return list_copy

print("The reserved list of {} is : {}".format(fruits, complicate_func_to_reserve(fruits, 1) ))

print(" \n============== Reverse a list, but only even positions ==============\n ")

fruits_larger = fruits.copy()
fruits_larger.append("peach")
fruits_larger.append("grapes")


print("The reserved list of {} is : {}".format(fruits, complicate_func_to_reserve(fruits, 2)))
print("The reserved list of {} is : {}".format(fruits_larger, complicate_func_to_reserve(fruits_larger, 2)))

print(" \n============== Extend the list ==============\n ")

fruits_larger.extend(["peach", "dragon fruit"])

print(fruits_larger)

print(" \n============== Sort a list ==============\n ")

fruits_larger.sort()
print("The sorted list is: {}".format(fruits_larger))


print(" \n============== Remove duplicates ==============\n ")

fruits_larger_2 = []

for n in fruits_larger:
    if n not in fruits_larger_2:
        fruits_larger_2.append(n)

fruits_larger = fruits_larger_2

print(fruits_larger)

###############################################################################################################################

numbers = [10, 20, 30, 40, 50, 60, 70]

print(" \n============== List slicing ==============\n ")
# Extract the first 3 elements and the last 2 elements using slicing.

numbers_3_2 = numbers[:3] + numbers[-3:]
print(numbers)
print(numbers_3_2)


print(" \n============== List comprehension ==============\n ")

# Generate a list of squares for numbers from 1 to 10.

squares_list = [n**2 for n in range(1,11)]

print(squares_list)


print(" \n============== Remove duplicates from a list ==============\n ")
# Write a function that removes duplicate values from a list.

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 10, 40, 50, 50]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)

print(" \n============== Find the maximum and minimum in a list ==============\n ")

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 10, 40, 50, 50, 10, 100, 0]

print(numbers)
print(max(numbers))
print(min(numbers))

sorted_numbers = numbers.copy()
sorted_numbers.sort()
print(sorted_numbers[-1])
print(sorted_numbers[0])


max1 = numbers[0]
min1 = numbers[0]

for n in numbers:
    if n > max1:
        max1 = n
    if n < min1:
        min1 = n

print(max1)
print(min1)

print(" \n============== Merge two lists ==============\n ")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1 + list2)

print(" \n============== Merge two lists ==============\n ")
# Given two lists, return a new list containing only the common elements.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6]
 
print([n for n in list1 if n in list2])

print(" \n============== Remove all occurrences of a value ==============\n ")
# Given a list, remove all occurrences of a specific value. Exaple: 0

numbers = [0, 10, 20, 30, 40, 50, 60, 0, 70, 10, 40, 50, 50, 10, 100, 0]
to_remove = 0

print([n for n in numbers if n != to_remove])

numbers_removed_0 = numbers.copy()

while 0 in numbers_removed_0:
    numbers_removed_0.remove(0)

print(numbers_removed_0)

print(" \n============== Sort a list of tuples ==============\n ")
# Sort the list based on grades in descending order.

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_students = students.copy()

sorted_students.sort(key=lambda item: item[1], reverse=True)

print(sorted_students)


print(" \n============== Flatten a nested list ==============\n ")

nested_list = [[1, 2], [3, 4], [5, 6]]

faltten_list = []

for n in nested_list:
    faltten_list.append(n[0])
    faltten_list.append(n[1])

print(faltten_list)

print([n for elem in nested_list for n in elem])

print(" \n============== Find missing numbers in a list ==============\n ")

numbers = [1, 2, 3, 5, 6, 9, 10]
missing_numbers = []

print([n for n in range(1, max(numbers) + 1) if n not in numbers])

print(" \n============== Rotate a list to the right (shiff 2 right) ==============\n ")
# Given a list [1, 2, 3, 4, 5], rotate it right by 2 positions to get [4, 5, 1, 2, 3].
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_shifted = numbers[-2:] + numbers[:-2]

print(numbers_shifted)


print(" \n============== Check if a list is sorted ==============\n ")
# Write a function to check if a list is sorted in ascending order.

numbers = [10, 20, 30, 40, 50, 60, 70, 10, 40, 50, 50, 10, 100, 0]

def is_sorted(numbers: list) -> bool:
    for n in range(0, len(numbers) - 1):
        if numbers[n+1] < numbers[n]:
            return False
    return True

print(is_sorted(numbers))
print(all(numbers[n + 1] >= numbers[n] for n in range(0, len(numbers) -1)))

numbers = [1,2,3,4,5,6,7,8,9]

print(is_sorted(numbers))

print(all(numbers[n + 1] >= numbers[n] for n in range(0, len(numbers) -1)))


print(" \n============== Split a list into two halves ==============\n ")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # len pair

half = int(len(numbers)/2)

num_1_half = numbers[:half]
num_2_half = numbers[half:]

print(num_1_half)
print(num_2_half)


print(" \n============== Group elements in a list ==============\n ")
# Given a list of numbers, group them into even and odd numbers using a dictionary.

numbers = [0, 1, 2, 10, 23, 20, 30, 40, 50, 7, 60, 70, 31, 21]

even_numbers = [n for n in numbers if n%2 == 0]
odd_numbers = [n for n in numbers if n%2 != 0]

print(even_numbers)
print(odd_numbers)

print(" \n============== Find the most frequent element in a list ==============\n ")
# Write a function that returns the most frequently occurring element in a list.


numbers = [10, 20, 20, 40, 50, 60, 70, 70, 40, 50, 50, 10, 100, 10, 100, 100]

def find_the_most_frequent_element_in_list(data: list) -> list:

    frequent_dict = {}

    for n in data:
        frequent_dict[n] = frequent_dict.get(n, 0) + 1

    most_frequent = max(frequent_dict.values())

    return [key for key, value in frequent_dict.items() if value==most_frequent]
    

print(find_the_most_frequent_element_in_list(numbers))


print(" \n============== Convert two lists into a dictionary ==============\n ")

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

dict_two = {}

for n in range(0, len(keys)):
    dict_two[keys[n]] = values[n]

print(dict_two)

#################################### DICTONARIES ################################


print("============== Create a dictionaty and assing keys and values==============\n")

students_grades = {
    "Alex": 88,
    "Max": 76,
    "Kevin": 70,
    "Kate": 99,
    "Bob": 50,
    "Tom": 45,
    "Melissa": 90,
    "David": 77,
}

print(" \n============== Print Melissa grade ============== ")

name = "Melissa"

if name in students_grades:
    print(students_grades[name])
else:
    print("\"{}\" NOR FOUND!".format(name))


print(
    " \n============== Print All people with their grades (iteration)) ============== "
)

for person in students_grades.items():
    print(person)

print(" \n============== Modify a value ( Kate : 100) ==============\n")
person = "Kate"

if person in students_grades:
    students_grades[person] = 100

print(students_grades)

print(" \n============== Add an element ( Daniel : 69) ==============\n")

new_name = "Daniel"
students_grades[new_name] = 69
print(students_grades)

print(" \n============== Remove an element (Daniel) ==============\n")

if new_name in students_grades:
    students_grades.__delitem__(new_name)
print(students_grades)

print(
    " ============== Fuction to check if Daniel was removed successfully =============="
)

if new_name not in students:
    print("{} was removed".format(new_name))
else:
    print("{} was not removed".format(new_name))

print(" \n============== Find the highest grade ==============\n")

print(max(students_grades.values()))

print(" \n============== Reverse a dictionary (Keys grades with names)==============\n")

reversed_dict = {}
for key, value in students_grades.items():
    reversed_dict[value] = key

print(reversed_dict)

print(" \n============== Merge two dictonaries into a single one ==============\n")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

dict_123 = dict1 | dict2 | dict3
print(dict_123)

dict_123.clear()
dict_123 = {**dict1, **dict2, **dict3}
print(dict_123)

dict_123.clear()
dict_123 = dict1.copy()
dict_123.update(dict2)
dict_123.update(dict3)
print(dict_123)


#######################################################################################################################################

products = {
    "apple": 500,
    "banana": 25,
    "pineapple": 1000,
    "watermelon": 2000,
    "tomato": 1000,
    "potato": 800,
    "strawberries": 1800,
    "grapes": 1600,
}

print(" \n============== Sort dictionary by values ==============\n")

print("Smallest to biggests: ")

sorted_products = dict(sorted(products.items(), key=lambda item: item[1]))
print(sorted_products)

print("biggests to Smallest: ")

sorted_products = dict(sorted(products.items(), key=lambda item: item[1], reverse=True))
print(sorted_products)


# Write a function to retrieve a user’s email.
print(" \n============== Nested dictionary lookup ==============\n")
users = {"john": {"age": 30, "email": "john@example.com"}}

print(users["john"]["email"])

print(" \n============== Find common keys in two dictionaries ==============\n")

products = {
    "apple": 500,
    "banana": 25,
    "pineapple": 1000,
    "watermelon": 2000,
    "tomato": 1000,
    "potato": 800,
    "strawberries": 1800,
    "grapes": 1600,
}
products2 = {
    "apple": 500,
    "banana": 25,
    "pineapple": 1000,
    "strawberries": 1800,
    "grapes": 1600,
    "beans": 800,
    "cheese": 2400,
    "beef": 4000,
}

print([product for product in products.keys() if product in products2.keys()])

print(" \n============== Check if a dictionary is empty ==============\n")

info = {"name": "Alice", "age": 25, "city": "New York"}
info2 = {}

print(not info)
print(not info2)

print(" \n============== Get the length of a dictionary ==============\n")

products = {
    "apple": 500,
    "banana": 25,
    "pineapple": 1000,
    "watermelon": 2000,
    "tomato": 1000,
    "potato": 800,
    "strawberries": 1800,
    "grapes": 1600,
}

print(products.__len__())
print(len(products.keys()))

print(" \n============== Create a dictionary from a list of keys ==============\n")

keys = ["name", "age", "city"]

dict_example = dict.fromkeys(keys)
print(dict_example)

print(" \n============== Find missing keys in a dictionary ==============\n")

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1}

print([n for n in dict1.keys() if n not in dict2.keys()])

print(
    " \n============== Remove duplicates from a list using a dictionary ==============\n"
)

data = ["a", "b", "b", "b", "c", "d", "e", "f", "g", "g", "h", "h", "i", "j", "k"]

print([list(dict.fromkeys(data))])

print(
    "Using cromprehension a dictionary of number from 1 to 5 and their squares"
)

print({n: n**2 for n in range(1,6)})


print(" \n============== Convert a list of tuples to a dictionary ==============\n")

tuple_list = [(1, "a"), (2, "b"), (3, "c")]

print(dict(tuple_list))

print(" \n============== Count frequency of characters in a string ==============\n")

data = "aabbbcccdddeeefffg"

freq_data = {}

for n in data:
    freq_data[n] = freq_data.get(n, 0) + 1

print(freq_data)

print(" \n============== Merge lists into a dictionary ==============\n ")

# If the lengths don't match, fill the missing values with None
keys = ["x", "y", "z", "a", "b"]
values = [10, 20, 30]

new_dict = {}

for n in range(0, len(keys)):

    if n < len(values):
        new_dict[keys[n]] = values[n]
    else:
        new_dict[keys[n]] = None

print(new_dict)


print(" \n============== Nested dictionary and list manipulation ==============\n ")
# Write a function that sums the values for each key and returns a dictionary with the sums.

data = {"a": [1, 2], "b": [3, 4], "c": [5, 6]}

data_sum = {}
for key, value in data.items():
    data_sum[key] = sum(value)

print(data_sum)

print(" \n============== Sort dictionary by key length ==============\n ")

# input: {'a': 1, 'abc': 2, 'ab': 3}
# output: {'a': 1, 'ab': 3, 'abc': 2}

data = {"a": 1, "abc": 2, "ab": 3, "abcd": 1}

data_sort = dict(sorted(data.items(), key= lambda item: len(item[0])))

print(data_sort)

##################################################################################################

people = {
    "Bob": {"ID": 1348, "surname": "Sccot", "Age": 28, "email": "bobscc@gmail.com"},
    "Alice": {
        "ID": 2357,
        "surname": "Johnson",
        "Age": 32,
        "email": "alice.johnson@hotmail.com",
    },
    "Charlie": {
        "ID": 7489,
        "surname": "Brown",
        "Age": 25,
        "email": "charlie.brown@yahoo.com",
    },
    "David": {
        "ID": 5623,
        "surname": "Smith",
        "Age": 40,
        "email": "david.smith@outlook.com",
    },
    "Emma": {
        "ID": 9812,
        "surname": "Williams",
        "Age": 29,
        "email": "emma.williams@example.com",
    },
    "Frank": {
        "ID": 6734,
        "surname": "Taylor",
        "Age": 35,
        "email": "frank.taylor@example.com",
    },
    "Grace": {
        "ID": 8451,
        "surname": "Anderson",
        "Age": 27,
        "email": "grace.anderson@gmail.com",
    },
} 



print(" \n============== Sort dictionary according to age ==============\n ")

def sort_according_to_some_paramether(dictionary: dict, parameter) ->  dict:

    if parameter is "name":
        return dict(sorted(dictionary.items(), key= lambda item: item[0]))

    else:
        return dict(sorted(dictionary.items(), key= lambda item: item[1][parameter]))

# print(sort_according_to_some_paramether(people, "Age"))

print(json.dumps(sort_according_to_some_paramether(people, "Age"), indent=4, sort_keys=False))


print(" \n============== Sort dictionary according to ID ==============\n ")

print(json.dumps(sort_according_to_some_paramether(people, "ID"), indent=4, sort_keys=False))

print(" \n============== Sort dictionary according to name ==============\n ")

print(json.dumps(sort_according_to_some_paramether(people, "name"), indent=4, sort_keys=False))

print(" \n============== Sort dictionary according to surname ==============\n ")

print(json.dumps(sort_according_to_some_paramether(people, "surname"), indent=4, sort_keys=False))


print(" \n============== Print all names (the dictionary keys). ==============\n ")

for key in people.keys():
    print(key)

print(" \n============== Print all emails of people in the dataset. ==============\n ")

for key, value in people.items():
    print(value["email"])

print(" \n============== Print the ID of Alice ==============\n ")

print(people["Alice"]["ID"])

print(" \n============== Print the surname of Grace ==============\n ")

print(people["Grace"]["surname"])

print(" \n============== Loop through the dataset and print each person's name and age ==============\n ")

for key, value in people.items():
    print("Name: {}  Age: {} ".format(key, value["Age"]))


print(" \n============== Find the youngest person in the dataset ==============\n ")

sorted_people = sorted(people.items(), key= lambda item: item[1]["Age"])
print(sorted_people[0][0])


print(" \n============== Find the oldest person in the dataset ==============\n ")

print(sorted_people[-1][0])

print(" \n============== Calculate the average age of all people ==============\n ")

print(statistics.mean([value["Age"] for value in people.values()]))


print(sum([value["Age"] for value in people.values()])/len(people))


print(" \n============== Print all names of people older than 30 ==============\n ")

print([(key, value["Age"]) for key, value in people.items() if value["Age"] > 30])

print("\n============== Check if \“Michael\” exists in the dataset. If not, print \"Not found\".==============\n ") 

if "Michael" in people.keys():
    print("Michael is in the dict")
else: 
    print("No found")

print(" \n============== Create a list of all IDs ==============\n ")

print([value["ID"] for value in people.values()])

print(" \n============== Find the person with the highest ID number ==============\n ")

print(max([value["ID"] for value in people.values()]))

print(" \n============== Sort all people by age (ascending) ==============\n ")


print(json.dumps(dict(sorted(people.items(),key= lambda item: item[1]["Age"])), indent=4, sort_keys=False))
 
print(" \n============== Sort all people by surname alphabetically ==============\n ")

print(json.dumps(dict(sorted(people.items(),key= lambda item: item[1]["surname"])), indent=4, sort_keys=False))

print(" \n============== Get a list of emails that end with @example.com ==============\n ")

print([value["email"] for value in people.values() if "@example.com" in value["email"]])

print(" \n============== Create a function that takes a name and returns the email ==============\n ")

def find_email_by_name(data: dict, name_s: str) -> str:

    if not data:
        print("Data set is emphty")
        return -1
    if name_s not in data:
        print("Name is not in data")
        return -1
    
    return "".join([value["email"] for key, value in data.items() if key==name_s])

print(find_email_by_name(people, "Frank"))

print(" \n============== Create a function that takes an ID and returns the person’s full name (Name + Surname) ==============\n ")

def get_fullname_by_ID(data:dict, ID: int) -> str:

    if not data:
        print("Data set is emphty")
        return -1
    if ID not in [value["ID"] for value in data.values()]:
        print("ID: {} is not in data".format(ID))
        return -1
    
    return "".join(["{} {}".format(key, value["surname"]) for key, value in data.items() if value["ID"]==ID])

print(get_fullname_by_ID(people, 7489))


print(" \n============== Add a new person to the dictionary dynamically ==============\n ")

USE_this = False
if USE_this == True:

    while True:
        ID = random.randint(1000, 9999)
        if ID not in [value["ID"] for value in people.values()]:
            print(ID)
            break


    name = input("Type the person's name: ")
    Surname = input("Type the person's surname: ")
    Age = input("Type the person's age: ")
    Email = input("Type the person's email: ")


    people[name] = {"ID": ID, "surname": Surname, "Age": Age, "email": Email}

    print(json.dumps(people, indent=4, sort_keys=True))

print(" \n============== Remove David from the dataset ==============\n ")

print(people.pop("David"))


print(" \n============== Create a new dictionary with only people under 30 years old. ==============\n ")

people_under_30 = people.copy()

for value in people_under_30.values():
    value["Age"] = random.randint(1, 29)

print(json.dumps(people_under_30, indent=4, sort_keys=True))


############################################################################################################################################################################

print("============== Swap Even Positions with Next One ==============")
# input str = "abcdfghi"
# output str = "badcgfih"
text = "abcdfghi"
text_l = list(text)
print(text)

for n in range(0, len(text_l) - 1, 2):
    text_l[n], text_l[n+1] = text_l[n+1], text_l[n]

print("".join(text_l))
print("".join(text[n:n+2][::-1] for n in range(0, len(text), 2)))


print("============== Reverse the String ==============")
# input str = "abcdfghi"
# output str = "ihgfdcba"
text = "abcdfghi"

print(text[::-1])

print("============== Check if a String is a Palindrome ==============")
# Input: "racecar"
# Output: True
text = "racecar"

print(text[::-1] == text)

print("============== Remove Vowels ==============")
# input str = "abcdfghiaaaaouuu"
# output str = "bcdfgh"

text = "abcdfghiaaaaouuu"

print("".join(n for n in text if n not in ["a", "e", "o", "i", "u"]))

print("============== Count Occurrences of Each Character ==============")
# input str = "abcdfghiaaaaouuu"
text = "abcdfffghiaaaaouuuf"

dict_text = {}

for n in text:
    dict_text[n] = dict_text.get(n, 0) + 1

print(dict_text)

print("============== Remove Duplicate Characters ==============")
# Input: "aabbcdeffg"
# Output: "abcdefg"
text = "aabbcdeffg"

print("".join(dict.fromkeys([n for n in text])))


print("============== Insert a Character at Every N Positions ==============")
# Input: "abcdfghi", N=2
# Output: "ab-cd-fg-hi"
text = "abcdfghid"
N=2

print("-".join([text[n:n+2] for n in range(0, len(text), 2)]))

print("============== Shift Characters to the Right==============")
# Input: "abcdfghi"
# Output: "iabcdfgh"
text = "abcdfghi"
N=1
N = N % len(text)
print(N)

print(text[-N:] + text[:-N])

print("============== Shift Characters to the Left==============")
# Input: "abcdfghi"
# Output: "bcdfghia"
text = "abcdfghi"
N=1

N = N % len(text)
print(N)

print(text[N:] + text[:N])

print("============== Remove a specific character ==============")
# Input: "abcdfghi"  R = "d"
# Output: "abcfghi"
text = "abcdfghi"
remove = "d"

text2 = text.replace(remove, "")
print(text2)

print("".join([n for n in text if n!=remove]))