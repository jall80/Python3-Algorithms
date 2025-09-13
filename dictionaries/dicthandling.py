# Autor: Jose Lopez Li
# Practice: Handling dictionaries in python

import json


def check_key_exist(key: str, dictionary: dict) -> bool:
    return key in dictionary.keys()


def find_highest_grade(dictionary: dict) -> dict:

    maxx = {"name": "", "grade": 0}
    for name, grade in dictionary.items():
        if grade > maxx["grade"]:
            maxx["grade"] = grade
            maxx["name"] = name
    return maxx


def find_highest_grade_OP(dictionary: dict) -> tuple[str, int]:
    if not dictionary:  # Check if the dictionary is empty
        return "No students", 0

    highest_student = max(
        dictionary, key=dictionary.get
    )  # Find the key with the highest value
    return highest_student, dictionary[highest_student]


def print_if_found(dictionary: dict, key: str):
    if key in dictionary:
        print("{}: {}".format(key, dictionary[key]))
    else:
        print("{} was not found in {}".format(key, dictionary))


def print_all_elements(dictionary: dict):
    if not dictionary:
        print(" The dictionary provided is empty")
    else:
        print(
            "\n".join(
                "{}: {}".format(name, grade) for name, grade in students_grades.items()
            )
        )


def print_all_elements_simpler(dictionary: dict):
    if not dictionary:
        print(" The dictionary provided is empty")
    else:
        for name, grade in students_grades.items():
            print("{}: {}".format(name, grade))


def add_or_modify_new_element(dictionary: dict, key: str, value: int):
    if not dictionary:
        print(" The dictionary provided is empty")
    elif key in dictionary:
        print(
            "The key: {} is already present with a value of : {}".format(
                key, dictionary[key]
            )
        )
        modify = ""
        while modify != "Y" and modify != "N":
            modify = input("Do you want to modify it? Type: Y / N: ")
        if modify == "Y":
            dictionary[key] = value
            print(
                "The value: ({}) has been assigned to the key: ({})".format(
                    dictionary[key], key
                )
            )
        elif modify == "N":
            print("Key ({}) value has not been modified".format(key))
        else:
            print("No input got from user, no key modified or added")
    else:
        dictionary[key] = value
        print(
            "New key ({}) was added with the value of: ({})".format(
                key, dictionary[key]
            )
        )


def delete_an_element_if_exists(dictionary: dict, key: str):
    if not dictionary:
        print(" The dictionary provided is empty")
    elif key not in dictionary:
        print("Tried to remove element but it is not present in {}".format(dictionary))
    else:
        del dictionary[key]
        if check_key_exist(key, dictionary):
            print("Element: {} WAS NOT successfully removed!".format(key))
        else:
            print("Element: {} was successfully removed".format(key))


def check_if_exists_in_dict(dictionary: dict, key: str):
    if not dictionary:
        print(" The dictionary provided is empty")
    else:
        print(
            "".join(
                "Key: ({}) exist in dict".format(key)
                if check_key_exist(key, students_grades)
                else "Key: ({}) doesn't exist in dict".format(key)
            )
        )


# there could be some replaced elements, if there are repeated values
def swap_keys_values(dictionary: dict) -> dict:
    result = {}
    if not dictionary:
        print(" The dictionary provided is empty")
    else:
        for key, value in dictionary.items():
            result[value] = key
    return result


def swap_keys_values_OP(dictionary: dict) -> dict:
    result = {}

    # Check if dictionary is empty and return an empty dictionary
    if not dictionary:
        print("The dictionary provided is empty")
        return result

    # Swap keys and values
    for key, value in dictionary.items():
        # If the value already exists as a key, store the key in a list
        if value in result:
            # If result[value] is not a list, convert it to a list
            if not isinstance(result[value], list):
                result[value] = [result[value]]
            result[value].append(key)
        else:
            result[value] = key

    return result


def merge_two_dicts(dict1: dict, dict2: dict) -> dict:
    merget_dict = dict1.copy()
    for key, value in dict2.items():
        merget_dict[key] = value
    return merget_dict


def sort_dictionary_by_values(dictionary: dict, rev=False) -> dict:

    list_dict = list(dictionary.items())
    list_dict.sort(key=lambda item: item[1], reverse=rev)

    return dict(list_dict)


def group_by_keys(data: list) -> dict:
    result = {}
    for n in data:
        if n[0] not in result:
            result[n[0]] = [n[1]]
        else:
            result[n[0]].append(n[1])
    return result


def find_common_keys(dict1: dict, dict2: dict) -> dict:
    common_keys = {}
    for key, value in dict1.items():
        if key in dict2:
            common_keys[key] = value
    return common_keys


def find_common_keysOP(dict1: dict, dict2: dict) -> dict:
    return {key: dict1[key] for key in dict1 if key in dict2}


def convert_two_lists_into_a_dictionary(list1: list, list2: list) -> dict:

    return {list1[n]: list2[n] if n < len(list2) else None for n in range(len(list1))}


def if_dict_empty(dictt: dict) -> bool:
    return not dictt


def count_items_dict(dictt: dict) -> int:
    return len(list(dictt.keys()))


def count_items_dictOP(dictt: dict) -> int:
    return len(dictt)


def find_missing_keys_dict(dictt1: dict, dictt2: dict) -> list:

    return [key for key in dictt1 if key not in dictt2]


def remove_duplicates_from_list(data: list) -> list:
    dict1 = dict.fromkeys(data)

    # When I convert to list to a dict, I only keep unique keys
    return [key for key in dict1]


def count_frequency_of_characters_in_string(data: str) -> dict:
    result = {}
    for char in data:
        result[char] = result.get(char, 0) + 1
    return result


def sum_values_for_each_key(data: dict) -> dict:

    return {key: sum(value) for key, value in data.items()}


def sort_dictionary_by_key_length(data: dict) -> dict:

    return dict(sorted(data.items(), key=lambda item: len(item[0])))


def sort_dictionary_according_to_parameter(data: dict, sort_param: str) -> dict:

    for key in data:
        if sort_param in data[key]:
            return dict(sorted(data.items(), key=lambda item: item[1][sort_param]))
        else:
            print(
                "Error: key {} is not part of dict: {}, cannot sort".format(
                    sort_param, data
                )
            )
            return None
'''
        
def sort_dictionary_according_to_parameter_recursive(data: dict, sort_param: str) -> dict:

    for key in data:
        if sort_param in data[key]:
            return dict(sorted(data.items(), key=lambda item: item[1][sort_param]))
        else:
            if data[key]:
                sort_dictionary_according_to_parameter_recursive(data[key], sort_param)
            else:
                return None

'''

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
print("The grade of {} is: ".format(input_name))
print_if_found(students_grades, input_name)

print(
    " \n============== Print All people with their grades (iteration)) ============== "
)

print_all_elements(students_grades)

print(
    " ============== Print All pwople with their grades (iteration simpler way) ============== "
)

print_all_elements_simpler(students_grades)

print(" \n============== Modify a value ( Kate : 100) ==============\n")

students_grades["Kate"] = 100
print("The new score of Kate is: {}".format(students_grades["Kate"]))

print(" \n============== Add an element ( Daniel : 69) ==============\n")

new_name = "Daniel"
add_or_modify_new_element(students_grades, "Daniel", 69)

print(" \n============== Remove an element (Daniel) ==============\n")

delete_an_element_if_exists(students_grades, new_name)

print(
    " ============== Fuction to check if Daniel was removed successfully =============="
)

check_if_exists_in_dict(students_grades, new_name)

print(
    " \n============== Fuction to check if Kate exists (She must exist) =============="
)

check_if_exists_in_dict(students_grades, "Kate")

print(" \n============== Find the highest grade ==============\n")

maxx = find_highest_grade(students_grades)
print(
    "Students: {} has the highest grade with a {}".format(maxx["name"], maxx["grade"])
)
max_name, max_grade = find_highest_grade_OP(students_grades)
print("Students: {} has the highest grade with a {}".format(max_name, max_grade))

print(" \n============== Reverse a dictionary (Keys grades with names)==============\n")

reverse_dict = swap_keys_values(students_grades)
# there could be some replaced elements, if there are repeated values
print("The revese dictionary of {} is ->>> {}".format(students_grades, reverse_dict))

print(" \n============== Merge two dictonaries into a single one ==============\n")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}
print(
    "Merging dicts: {} + {} ====>  {}".format(
        dict1, dict2, merge_two_dicts(dict1, dict2)
    )
)
merged_dicts = dict1.copy()
merged_dicts.update(dict2)
print("Merging dicts: {} + {} ====>  {}".format(dict1, dict2, merged_dicts))
merged_dict = {}
merged_dicts = {**dict1, **dict2, **dict3}  # ** unpack operator
print("Merging dicts: {} + {} + {} ====>  {}".format(dict1, dict2, dict3, merged_dicts))
merged_dict = {}
merged_dict = dict1 | dict2 | dict3  # union operator
print("Merging dicts: {} + {} + {} ====>  {}".format(dict1, dict2, dict3, merged_dicts))

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
print("The sorted dictionary is ===> {}".format(sorted_products))

print("Biggests to smallest: ")
sorted_products = dict(sorted(products.items(), key=lambda item: item[1], reverse=True))
print("The sorted dictionary is ===> {}".format(sorted_products))

print("Smallest to biggests: ")
sorted_products = {}
sorted_products = sort_dictionary_by_values(products)
print("The sorted dictionary is ===> {}".format(sorted_products))

print(" \n============== Group by keys ==============\n")
fruits = [("apple", 3), ("banana", 2), ("apple", 5), ("banana", 1)]

data_dict = group_by_keys(fruits)
print("From list: {}, the dictionary resulted is: {}".format(fruits, data_dict))

# Write a function to retrieve a user’s email.
print(" \n============== Nested dictionary lookup ==============\n")
users = {"john": {"age": 30, "email": "john@example.com"}}
print("The email of {} is: {}".format("john", users["john"]["email"]))

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

print(
    "The following keys are present in both dict {} AND {} ====> {}".format(
        products, products2, find_common_keys(products, products2)
    )
)
print(
    "The following keys are present in both dict {} AND {} ====> {}".format(
        products, products2, find_common_keysOP(products, products2)
    )
)


print(" \n============== Convert two lists into a dictionary ==============\n")

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

dictionary = convert_two_lists_into_a_dictionary(keys, values)

print(
    "The dictionary froms lists {} and {} is ===> {}".format(keys, values, dictionary)
)

dictionary.clear()
dictionary = dict(
    zip(keys, values)
)  # ONLY IF BOTH LISTS HAVE SAVE LENGHT, OTHERWISE KEYS WITHOUT MATCHING VALUE WILL BE REMOVED.

print(
    "The dictionary froms lists {} and {} is ===> {}".format(keys, values, dictionary)
)

print(" \n============== Check if a dictionary is empty ==============\n")

info = {"name": "Alice", "age": 25, "city": "New York"}
info2 = {}

print("Dict: {} is empty ===> {}".format(info, if_dict_empty(info)))
print("Dict: {} is empty ===> {}".format(info2, if_dict_empty(info2)))

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

print(
    "The lengh of the dict: {} is ===> {}".format(products, count_items_dict(products))
)
print(
    "The lengh of the dict: {} is ===> {}".format(
        products, count_items_dictOP(products)
    )
)

print(" \n============== Create a dictionary from a list of keys ==============\n")

keys = ["name", "age", "city"]
dict_from_keys = dict.fromkeys(keys)

print("The dictionary resulted from keys = {} is ====> {}".format(keys, dict_from_keys))

print(" \n============== Find missing keys in a dictionary ==============\n")

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1}

print(
    "The missing keys in {} from {} are ===> {}".format(
        dict2, dict1, find_missing_keys_dict(dict1, dict2)
    )
)

print(
    "The missing keys in {} from {} are ===> {}".format(
        dict1, dict2, find_missing_keys_dict(dict2, dict1)
    )
)

print(
    " \n============== Remove duplicates from a list using a dictionary ==============\n"
)

data = ["a", "b", "b", "b", "c", "d", "e", "f", "g", "g", "h", "h", "i", "j", "k"]

print(
    "From list: {}, the resulted list without repeated elements is ===> {}".format(
        data, remove_duplicates_from_list(data)
    )
)

print(" \n============== Dictionary comprehension ==============\n")

dictionary = {n: n**2 for n in range(1, 6)}

print(
    "Using cromprehension a dictionary of number from 1 to 5 and their squares is ===> {}".format(
        dictionary
    )
)

print(" \n============== Convert a list of tuples to a dictionary ==============\n")

tuple_list = [(1, "a"), (2, "b"), (3, "c")]
dict1 = dict(tuple_list)

print(
    "From the tuples list: {} the resulted dictionary is ===> {}".format(
        tuple_list, dict1
    )
)

print(" \n============== Count frequency of characters in a string ==============\n")

data = "aabbbcccdddeeefffg"

print(
    "From string : '{}' the dictonary is ===> {}".format(
        data, count_frequency_of_characters_in_string(data)
    )
)

print(" \n============== Merge lists into a dictionary ==============\n ")

# If the lengths don't match, fill the missing values with None
keys = ["x", "y", "z", "a", "b"]
values = [10, 20, 30]

dictionary = convert_two_lists_into_a_dictionary(keys, values)

print(
    "The dictionary froms lists {} and {} is ===> {}".format(keys, values, dictionary)
)

print(" \n============== Nested dictionary and list manipulation ==============\n ")
# Write a function that sums the values for each key and returns a dictionary with the sums.

data = {"a": [1, 2], "b": [3, 4], "c": [5, 6]}

print(
    " From dict: {} the resulted dict with the sum of values is ===> {}".format(
        data, sum_values_for_each_key(data)
    )
)

print(" \n============== Sort dictionary by key length ==============\n ")

# input: {'a': 1, 'abc': 2, 'ab': 3}
# output: {'a': 1, 'ab': 3, 'abc': 2}

data = {"a": 1, "abc": 2, "ab": 3}

print(
    "From list: {} the sorted list according to keys lenght is: {}".format(
        data, sort_dictionary_by_key_length(data)
    )
)
##################################################################################################

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

people_sort = sort_dictionary_according_to_parameter(people, "Age")

print(
    "The sorted dictionary according to {} is ===>\n {}".format(
        "Age", json.dumps(people_sort, indent=4, sort_keys=False)
    )
)

print(" \n============== Sort dictionary according to ID ==============\n ")

people_sort = sort_dictionary_according_to_parameter(people, "ID")

print(
    "The sorted dictionary according to {} is ===>\n {}".format(
        "ID", json.dumps(people_sort, indent=4, sort_keys=False)
    )
)

print(" \n============== Sort dictionary according to name ==============\n ")

print(
    "The sorted dictionary according to {} is ===>\n {}".format(
        "name", json.dumps(people, indent=4, sort_keys=True)
    )
)

print(" \n============== Sort dictionary according to surname ==============\n ")

people_sort = sort_dictionary_according_to_parameter(people, "surname")

print(
    "The sorted dictionary according to {} is ===>\n {}".format(
        "surname", json.dumps(people_sort, indent=4, sort_keys=False)
    )
)
