# Datatypes
# - numeric: int, float, complex
# - dictionary
# - boolean
# - set
# - sequence type: stings, list, tuple

# Numeric
num1 = 10
num2 = 20.5
num3 = 10 + 20j

# Dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Boolean
is_valid = True
is_invalid = False

# Set
fruit_set = {"apple", "banana", "orange"}

# Sequence type
numbers = [1, 2, 3, 4, 5]
strings = ["apple", "banana", "orange"]
tuples = (1, 2, 3, 4, 5)

# Accessing elements
print(numbers[0])  # Output: 1
print(strings[1])  # Output: banana
print(tuples[2])  # Output: 3

# Modifying elements
numbers[0] = 100
strings[1] = "grape"
tuples = tuples[:2] + (6,) + tuples[2:]  # (1, 2, 6, 4, 5) -> (1, 2, 6, 4, 5) + (6,) -> (1, 2, 6, 4, 5, 6)

print(numbers)  # Output: [100, 3, 4, 5]
print(strings)  # Output: ['apple', 'grape', 'orange']
print(tuples)  # Output: (1, 2, 6, 4, 5)

# Adding elements
numbers.append(6)
strings.insert(1, "melon")
tuples += (7,)

print(numbers)  # Output: [100, 3, 4, 5, 6]
print(strings)  # Output: ['apple', 'melon', 'grape', 'orange']
print(tuples)  # Output: (1, 2, 6, 4, 5, 7)

# Removing elements
numbers.remove(6)
strings.pop(1)
tuples = tuples[:-1]

print(numbers)  # Output: [100, 3, 4, 5]
print(strings)  # Output: ['apple', 'orange']
print(tuples)  # Output: (1, 2, 4, 5)

# Length of a sequence
print(len(numbers))  # Output: 4
print(len(strings))  # Output: 3
print(len(tuples))  # Output: 4

# Concatenation
concatenated_strings = strings + ["cherry", "kiwi"]
concatenated_tuples = tuples + (8,)

print(concatenated_strings)  # Output: ['apple', 'orange', 'cherry', 'kiwi']
print(concatenated_tuples)  # Output: (1, 2, 4, 5, 8)

# Repetition
repeated_strings = strings * 2
repeated_tuples = tuples * 3

print(repeated_strings)  # Output: ['apple', 'orange', 'apple', 'orange']
print(repeated_tuples)  # Output: (1, 2, 4, 5, 1, 2, 4, 5, 4, 5)

# Membership test
print("apple" in strings)  # Output: True
print(10 in numbers)  # Output: False

# Slicing
sliced_strings = strings[1:3]
sliced_tuples = tuples[1:3]

print(sliced_strings)  # Output: ['orange', 'apple']
print(sliced_tuples)  # Output: (2, 4)

# Sorting
sorted_strings = sorted(strings)
sorted_tuples = sorted(tuples)

print(sorted_strings)  # Output: ['apple', 'banana', 'orange']
print(sorted_tuples)  # Output: (1, 2, 3, 4, 5)

# Reverse
reversed_strings = sorted_strings[::-1]
reversed_tuples = sorted_tuples[::-1]

print(reversed_strings)  # Output: ['orange', 'banana', 'apple']
print(reversed_tuples)  # Output: (5, 4, 3, 2, 1)

# Searching
index_of_apple = strings.index("apple")
index_of_1 = numbers.index(1)

print(index_of_apple)  # Output: 0
print(index_of_1)  # Output: 0

# Counting
count_of_apple = strings.count("apple")
count_of_1 = numbers.count(1)

print(count_of_apple)  # Output: 1
print(count_of_1)  # Output: 1

# Min and max
min_value_in_numbers = min(numbers)
max_value_in_numbers = max(numbers)

print(min_value_in_numbers)  # Output: 3
print(max_value_in_numbers)  # Output: 100

# List comprehension
squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)  # Output: [9, 9, 16, 25, 10000]

# Dictionary comprehension
squared_numbers_dict = {num: num ** 2 for num in numbers}

print(squared_numbers_dict)  # Output: {10: 100, 20: 400, 30: 900, 40: 1600, 50: 2500}

# Set comprehension
squared_numbers_set = {num ** 2 for num in numbers}

print(squared_numbers_set)  # Output: {100, 9, 400, 900, 1600, 2500, 10000}

# Generator expression
squared_numbers_generator = (num ** 2 for num in numbers)

for num in squared_numbers_generator:
    print(num)  # Output: 9, 9, 16, 25, 10000

# Lambda function
square = lambda num: num ** 2

print(square(10))  # Output: 100

# Map function
squared_numbers_map = list(map(square, numbers))

print(squared_numbers_map)  # Output: [9, 9, 16, 25, 10000]

# Filter function
even_numbers_filter = list(filter(lambda num: num % 2 == 0, numbers))

print(even_numbers_filter)  # Output: [10, 20, 40, 10000]

# Zip function
numbers_and_strings = list(zip(numbers, strings))

print(numbers_and_strings)  # Output: [(10, 'apple'), (20, 'banana'), (30, 'orange')]

# Enumerate function
enumerated_numbers = list(enumerate(numbers))

print(enumerated_numbers)  # Output: [(0, 10), (1, 20), (2, 30), (3, 40), (4, 10000)]

# Unpacking
num1, num2, *others = numbers

print(num1)  # Output: 10
print(num2)  # Output: 20
print(others)  # Output: [30, 40, 10000]

# Tuple unpacking
numbers_tuple = (10, 20, 30, 40, 10000)
num1, num2, *others = numbers_tuple

print(num1)  # Output: 10
print(num2)  # Output: 20
print(others)  # Output: [30, 40, 10000]

# Deleting variables
del num1, num2, others

try:
    print(num1)  # Output: NameError: name 'num1' is not defined
except NameError as e:
    print(e)