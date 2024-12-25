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