
print(" \n============== Remove duplicates from a list ==============\n ")

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 10, 40, 50, 50]

print(list(set(numbers)))

print(" \n============== Merge two lists ==============\n ")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1 + list2)

print(" \n============== Remove all occurrences of a value ==============\n ")
# Given a list, remove all occurrences of a specific value. Example: 0

numbers = [0, 10, 20, 30, 40, 50, 60, 0, 70, 10, 40, 50, 50, 10, 100, 0]

numbers_rev = [n for n in numbers if n != 0]

print(numbers_rev)

print(" \n============== Sort a list of tuples ==============\n ")
# Sort the list based on grades in descending order.

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]

students_sort = sorted(students, key=lambda x: x[1])

print(students_sort)

print(" \n============== Flatten a nested list ==============\n ")

nested_list = [[1, 2], [3, 4], [5, 6]]

flatten_list = [n for elem in nested_list for n in elem]

print(flatten_list)

print(" \n============== Find missing numbers in a list ==============\n ")

numbers = [1, 2, 3, 5, 6, 9, 10]

missing_numbers = [n for n in range(min(numbers), max(numbers)) if n not in numbers]

print(missing_numbers)

print(" \n============== Rotate a list to the right (shiff 2 right) ==============\n ")
# Given a list [1, 2, 3, 4, 5], rotate it right by 2 positions to get [4, 5, 1, 2, 3].
numbers = [1, 2, 3, 4, 5]

n = 2
numbers = numbers[-n:] + numbers[:-n]
print(numbers)


###########################################################################################################################################

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
input_name = "Melissa"


print(students_grades[input_name])

print(" \n============== Add an element ( Daniel : 69) ==============\n")

students_grades["Daniel"] = 69
print(students_grades["Daniel"])

print(" \n============== Remove an element (Daniel) ==============\n")

del students_grades["Daniel"]

print(
    " ============== Fuction to check if Daniel was removed successfully =============="
)

def check_elem_in_dict(names:dict, name:str) -> bool:

    return name in names

print(check_elem_in_dict(students_grades, "Daniel"))


print(" \n============== Find the highest grade ==============\n")

print(max(students_grades.items(), key=lambda item: item[1]))

print(" \n============== Find the lowest grade ==============\n")

print(min(students_grades.items(), key=lambda item: item[1]))


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

sorted_products = dict(sorted(products.items(), key=lambda x: x[1]))
print(sorted_products)

print("Biggests to smallest: ")

sorted_products = dict(sorted(products.items(), key=lambda x: x[1], reverse=True))
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

common_keys = [n for n in products if n in products2]
print(common_keys)


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

print("The leght of the dictionary is {}".format(len(products)))

print(" \n============== Create a dictionary from a list of keys ==============\n")

keys = ["name", "age", "city"]
values = ["Ana", 18, "Cartago"]

dict_new = dict.fromkeys(keys)
print(dict_new)

print(
    " \n============== Remove duplicates from a list using a dictionary ==============\n"
)

data = ["a", "b", "b", "b", "c", "d", "e", "f", "g", "g", "h", "h", "i", "j", "k"]

data_no_duplicates = list(dict.fromkeys(data))
print(data_no_duplicates)

print(" \n============== Convert a list of tuples to a dictionary ==============\n")

tuple_list = [(1, "a"), (2, "b"), (3, "c")]

dict_new = dict(tuple_list)
print(dict_new)

print(" \n============== Count frequency of characters in a string ==============\n")

data = "aabbbcccdddeeefffg"

dict_count = {}
for n in data:
    dict_count[n] = dict_count.get(n, 0) + 1

print(dict_count)


print(" \n============== Nested dictionary and list manipulation ==============\n ")
# Write a function that sums the values for each key and returns a dictionary with the sums.

data = {"a": [1, 2], "b": [3, 4], "c": [5, 6]}

def sum_lists_in_dict(data:dict) -> dict:

    data_sum = {}
    for key, value in data.items():
        data_sum[key] = sum(value)
    return data_sum

print(sum_lists_in_dict(data))


people = {
    "Bob": {"ID": 1348, "surname": "Sccot", "Age": 28, "email": "bobscc@gmail.com"},
    "Alice": {
        "ID": 2357,
        "surname": "Johnson",
        "Age": 32,
        "email": "alice.johnson@example.com",
    },
    "Charlie": {
        "ID": 7489,
        "surname": "Brown",
        "Age": 25,
        "email": "charlie.brown@example.com",
    },
    "David": {
        "ID": 5623,
        "surname": "Smith",
        "Age": 40,
        "email": "david.smith@example.com",
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
        "email": "grace.anderson@example.com",
    },
} 


print(" \n============== Sort dictionary according to age ==============\n ")

def sort_dict_age(data:dict) -> dict:

    return sorted(data.items(), key= lambda x: x[1]["Age"])

print(sort_dict_age(people))


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None 

# ==============================
# 5. Preorder Tree Traversal – O(n)
# ==============================
# Recorre un árbol binario en el orden: Root → Left → Right

# INSERT
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def preorder(root):
    if root:
        print(root.value, end = " -> ")
        preorder(root.left)
        preorder(root.right)

def in_order(root):
    if root:
        in_order(root.left)
        print(root.value, end = " -> ")
        in_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value, end = " -> ")

def search_in_tree(root, value):
    if root:
        if root.value == value:
            return True
        return search_in_tree(root.left, value) or search_in_tree(root.right, value)
    return False

values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
root = None

for val in values:
    root = insert(root, val)

print("\nPre-order traversal (Root → Left → Right):")
preorder(root)

print("In-order traversal (Left → Root → Right):")
in_order(root)

print("\nPost-order traversal (Left → Right → Root):")
post_order(root)

print("\n\nSearch for 6:")

print(search_in_tree(root, 13))


