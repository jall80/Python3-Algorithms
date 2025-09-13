# Autor: Jose Lopez Li
# Practice: Handling lists in python


def check_list(func):
    def wrapper(*args, **kwargs):  # Accepts any arguments
        if (
            args and isinstance(args[0], list) and args[0]
        ):  # /Check an argument is sent/Check this argument is a list/ Check that this list isnot empty
            return func(*args, **kwargs)
        else:
            raise ValueError(
                "It's not possible to execute the function because the provided list is empty."
            )

    return wrapper


@check_list
def update_list(data: list, index: int, value: str):
    data[index] = value


@check_list
def return_value_list(data: list, index: int):
    return data[index]


@check_list
def find_value_index(data: list, value: str) -> int:

    if value not in data:
        print("Error: Value: {} not found in list; {}".format(value, data))
        return None
    else:
        return int("".join(str(n) for n in range(len(data)) if data[n] == value))


@check_list
def change_value(data: list, value: str, new_value: str):
    if value not in data:
        print(
            "Warning: Cannot replace. Value: '{}' doesn't exist in list: ==> {}".format(
                value, data
            )
        )
    else:
        data[find_value_index(data, value)] = new_value

@check_list
def is_in_list(data: list, value: str) -> bool:
    return value in data

@check_list
def reverse_list(data: list, step: int) -> list:
    for n in range(0, int(len(data) / 2), step):
        data[n], data[-1 - n] = data[-1 - n], data[n]
    return data

@check_list
def remove_duplicates_from_list(data: list) -> list:
    result = []
    for n in data:
        if n not in result:
            result.append(n)
    return result


@check_list
def remove_duplicates_from_listOP(data: list) -> list:
    return list(dict.fromkeys(data))  # Keeps order while removing duplicates


@check_list
def flatten_nested_list(data: list) -> list:
    result = []
    for n in data:
        for elem in n:
            result.append(elem)
    return result


@check_list
def check_if_ist_is_sorted_asc(data: list) -> bool:
    return all(data[n] <= data[n + 1] for n in range(len(data) - 1))


@check_list
def check_if_ist_is_sorted_des(data: list) -> bool:
    return all(data[n] >= data[n + 1] for n in range(len(data) - 1))


@check_list
def returns_the_second_largest_number(data: list) -> int:
    sorted_data = data.copy()
    sorted_data.sort()

    # Delete any max element from the list
    clean_data = [n for n in sorted_data if n != sorted_data[-1]]

    return clean_data[-1]


@check_list
def returns_the_second_largest_numberOP(data: list) -> int:
    sorted_data = sorted(set(data))  # Sort and remove duplicates

    if len(sorted_data) < 2:  # Handle cases with only one unique number
        raise ValueError("List must contain at least two distinct numbers.")

    return sorted_data[-2]  # Return the second largest


@check_list
def find_the_most_frequent_element_in_list(data: list) -> list:

    frequency_dict = {}
    for n in data:
        frequency_dict[n] = frequency_dict.get(n, 0) + 1

    max_freq = max(frequency_dict.values())

    return [key for key, value in frequency_dict.items() if value == max_freq]


@check_list
def detect_sequence(data: list) -> int:
    if (
        len(set(data)) < 2
    ):  # Handle edge case where there's not enough data to determine a step
        return 0

    dict_diferences = {}
    sorted_data = sorted(set(data))

    for n in range(1, len(sorted_data)):
        diff = sorted_data[n] - sorted_data[n - 1]
        dict_diferences[diff] = dict_diferences.get(diff, 0) + 1

    return max(dict_diferences, key=dict_diferences.get)


@check_list
def find_missing_number(data: list) -> list:
    step = detect_sequence(data)
    if step == 0:
        return []  # If no valid sequence is detected, return an empty list

    sorted_data = sorted(set(data))

    return [
        n
        for n in range(sorted_data[0], sorted_data[-1] + step, step)
        if n not in sorted_data
    ]


@check_list
def remove_no_in_sequence(data: list, step: int) -> list:
    if step == 0 or not data:
        return []  # Avoid errors when step is 0 or data is empty

    sorted_data = sorted(set(data))
    start = sorted_data[0]  # Define the sequence start point dynamically

    return sorted(set(n for n in data if (n - start) % step == 0))


#############################################################################################################################
print(" \n============== Create a list of five fruits. ==============\n ")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("The created list: {}".format(fruits))

print(" \n============== Access elements ==============\n ")
# print the first and last elements

print(
    "The first and last element is: {} and {}".format(
        return_value_list(fruits, 0), return_value_list(fruits, -1)
    )
)

print(" \n============== Modify elements ==============\n ")
# Change 'banana' to 'blueberry' in the list

# if I know the index of banana
# fruits[1] = "blueberry"
update_list(fruits, 1, "blueberry")
print("Changing banana to blueberry is list ==> {}".format(fruits))

update_list(fruits, 1, "banana")
# Better way and if I don't know the banana index
value = "banana"
new_value = "blueberry"

change_value(fruits, value, new_value)
print("Changing banana to blueberry is list ==> {}".format(fruits))

print(" \n============== Check if an element exists ==============\n ")

print(" Does 'peach' exist in list? {}".format(is_in_list(fruits, "peach")))
print(" Does 'apple' exist in list? {}".format(is_in_list(fruits, "apple")))

print(" \n============== Reverse a list ==============\n ")

# Simplest method
reversed_list = fruits[::-1]
print("The reversed list is: {}".format(reversed_list))
  
# Working in algorim
print("The reversed list is: {}".format(reverse_list(fruits, 1)))

print(" \n============== Reverse a list, but only even positions ==============\n ")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits2 = ["peach", "strawberry", "watermelon", "grape", "dragonfruit"]

fruit_large = fruits + fruits2

# Working in algorim
print("The reversed list in even positions is: {}".format(reverse_list(fruit_large, 2)))

print(" \n============== Sort a list ==============\n ")

fruit_large.sort()
print("The sorted list is: {}".format(fruit_large))

print(" \n============== List length ==============\n ")

print(
    "The lenght of the list is: {},  for list: {}".format(len(fruit_large), fruit_large)
)

###############################################################################################################################

numbers = [10, 20, 30, 40, 50, 60, 70]

print(" \n============== List slicing ==============\n ")
# Extract the first 3 elements and the last 2 elements using slicing.

print(
    "From list: {}, the first three elements are: {} and the last two elements are: {}".format(
        numbers, numbers[0:3], numbers[-2:]
    )
)

print(" \n============== List comprehension ==============\n ")

# Generate a list of squares for numbers from 1 to 10.

print(
    "A list from squares for numbers from 1 to 10 is: {}".format(
        [n**2 for n in range(1, 11)]
    )
)

print(" \n============== Remove duplicates from a list ==============\n ")
# Write a function that removes duplicate values from a list.

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 10, 40, 50, 50]
numbers = remove_duplicates_from_list(numbers)

print("The list without duplicate elements is: {}".format(numbers))

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 10, 40, 50, 50]
numbers = remove_duplicates_from_listOP(numbers)

print("The list without duplicate elements is: {}".format(numbers))

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 10, 40, 50, 50]

print("with SET The list without duplicate elements is: {}".format(list(set(numbers))))

print(" \n============== Find the maximum and minimum in a list ==============\n ")

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 10, 40, 50, 50, 10, 100, 0]
numbers_sorted = numbers
numbers_sorted.sort()

print(
    "The maximum number is: {} and the minimum number is: {}".format(
        numbers_sorted[-1], numbers_sorted[0]
    )
)

print(" \n============== Merge two lists ==============\n ")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(
    "The resulted list fo merging {} and {} is ===> {}".format(
        list1, list2, list1 + list2
    )
)

print(" \n============== Merge two lists ==============\n ")
# Given two lists, return a new list containing only the common elements.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6]

print(
    "The elements contained by list: {} and {} are ===> {}".format(
        list1, list2, [n for n in list1 if n in list2]
    )
)

print(" \n============== Remove all occurrences of a value ==============\n ")
# Given a list, remove all occurrences of a specific value. Exaple: 0

numbers = [0, 10, 20, 30, 40, 50, 60, 0, 70, 10, 40, 50, 50, 10, 100, 0]

print("List {} without zeros is ===>{}".format(numbers, [n for n in numbers if n != 0]))

# Other way
numbers_without_zeros = numbers.copy()
while 0 in numbers_without_zeros:
    numbers_without_zeros.remove(0)

print("List {} without zeros is ===>{}".format(numbers, numbers_without_zeros))


######################################################################################################

print(" \n============== Sort a list of tuples ==============\n ")
# Sort the list based on grades in descending order.

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_students = students.copy()

sorted_students.sort(key=lambda item: item[1], reverse=True)

print(
    "From list {}, the sorted list according to grades is: {}".format(
        students, sorted_students
    )
)

print(" \n============== Flatten a nested list ==============\n ")

nested_list = [[1, 2], [3, 4], [5, 6]]

print(
    "From list: {}, the flatted is ===> {}".format(
        nested_list, [elem for n in nested_list for elem in n]
    )
)

flatten_list = flatten_nested_list(nested_list)

print("From list: {}, the flatted is ===> {}".format(nested_list, flatten_list))

print(" \n============== Find missing numbers in a list ==============\n ")

numbers = [1, 2, 3, 5, 6, 9, 10]

print(
    "From list: {}, from 1 to 10 the missing numbers are ===> {}".format(
        numbers, [n for n in range(1, 11) if n not in numbers]
    )
)

print(" \n============== Rotate a list to the right (shiff 2 right) ==============\n ")
# Given a list [1, 2, 3, 4, 5], rotate it right by 2 positions to get [4, 5, 1, 2, 3].
numbers = [1, 2, 3, 4, 5]

n = 2
n = n % len(numbers)
print(numbers[-n:] + numbers[:-n])

print(" \n============== Check if a list is sorted ==============\n ")
# Write a function to check if a list is sorted in ascending order.

numbers = [10, 20, 30, 40, 50, 60, 70, 10, 40, 50, 50, 10, 100, 0]
numbers_sorted_asc = [1, 2, 3, 5, 6, 9, 10]
numbers_sorted_des = [10, 8, 5, 4, 2, 0]

print(
    "Is list: {} sorted ascending ===> {}".format(
        numbers, check_if_ist_is_sorted_asc(numbers)
    )
)
print(
    "Is list: {} sorted ascending ===> {}".format(
        numbers_sorted_asc, check_if_ist_is_sorted_asc(numbers_sorted_asc)
    )
)
print(
    "Is list: {} sorted descending ===> {}".format(
        numbers_sorted_des, check_if_ist_is_sorted_des(numbers_sorted_des)
    )
)

print(" \n============== Split a list into two halves ==============\n ")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # len pair

print("First half: ")
print(numbers[: len(numbers) // 2 + (1 if len(numbers) % 2 != 0 else 0)])

print("Second half: ")
print(numbers[len(numbers) // 2 + (1 if len(numbers) % 2 != 0 else 0) :])


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # len odd +1 element if first list


print("First half: ")
print(numbers[: len(numbers) // 2 + (1 if len(numbers) % 2 != 0 else 0)])

print("Second half: ")
print(numbers[len(numbers) // 2 + (1 if len(numbers) % 2 != 0 else 0) :])

print(" \n============== Find the second largest number in a list ==============\n ")

numbers = [10, 20, 30, 40, 50, 60, 70, 10, 40, 50, 50, 10, 100, 0, 100, 100]
print(
    "The second higest number in the list {} is ====> {}".format(
        numbers, returns_the_second_largest_number(numbers)
    )
)
print(
    "The second higest number in the list {} is ====> {}".format(
        numbers, returns_the_second_largest_numberOP(numbers)
    )
)

print(" \n============== Group elements in a list ==============\n ")
# Given a list of numbers, group them into even and odd numbers using a dictionary.

numbers = [0, 1, 2, 10, 23, 20, 30, 40, 50, 7, 60, 70, 31, 21]

odd_numbers = [n for n in numbers if n % 2 != 0]
even_numbers = [n for n in numbers if n % 2 == 0]

print("The list of odd numbers is: {}".format(odd_numbers))
print("The list of even numbers is: {}".format(even_numbers))

print(" \n============== Find the most frequent element in a list ==============\n ")
# Write a function that returns the most frequently occurring element in a list.


numbers = [10, 20, 20, 40, 50, 60, 70, 70, 40, 50, 50, 10, 100, 10, 100, 100]

print(
    "The most reapted number in list: {} is: {}".format(
        numbers, find_the_most_frequent_element_in_list(numbers)
    )
)


print(" \n============== Convert two lists into a dictionary ==============\n ")

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

dict_list = {key: value for key in keys for value in values}

print(
    "The resulted dictionary from keys {} and values {} is ====> {}".format(
        keys, values, dict_list
    )
)

print(" \n============== Find the sequence in the list ==============\n ")

numbers = [1, 4, 6, 2, 7, 1, 9, 5, 8, 0]

print(
    "The sequence is the list: {} is ====> in {} steps".format(
        numbers, detect_sequence(numbers)
    )
)

numbers = [0, 6, 4, 6, 8, 0, 3, 10]

print(
    "The sequence is the list: {} is ====> in {} steps".format(
        numbers, detect_sequence(numbers)
    )
)


print(" \n============== Remove elements no in sequence ==============\n ")

numbers = [0, 6, 6, 8, 0, 3, 10, 12]
step = detect_sequence(numbers)
numbers_sequenced = remove_no_in_sequence(numbers, step)
print(
    "From list {} the list sorted and in sequence ({}) is ===> {}".format(
        numbers, step, numbers_sequenced
    )
)


print(" \n============== Find the missing number in sequence ==============\n ")

numbers = [1, 4, 6, 2, 7, 1, 9, 5, 8, 0]

print(
    "The missing numbers in list: {} are ===> {}".format(
        numbers, find_missing_number(numbers)
    )
)

print(
    "The missing numbers in list: {} are ===> {}".format(
        numbers_sequenced, find_missing_number(numbers_sequenced)
    )
)

print(
    " \n============== Detect / Sequence / Remove no in sequence / Get missing numbers in sequence ==============\n "
)

numbers = [5, 7, 10, 15, 22, 30, 35]
step = detect_sequence(numbers)
numbers_sequenced = remove_no_in_sequence(numbers, step)
print(
    "From list {} the list sorted and in sequence ({}) are ===> {}".format(
        numbers, step, numbers_sequenced
    )
)
print(
    "The missing numbers in list: {} is ===> {}".format(
        numbers_sequenced, find_missing_number(numbers_sequenced)
    )
)
