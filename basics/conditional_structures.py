# Conditional Structures
# - if
# - loops
# - break and continue

# if statement
if 5 > 3:
    print("Five is greater than three")

# loops
for i in range(5):
    print(i)

# break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)

# Nested if statement
x = 10
y = 20
if x > 5:
    if y > 10:
        print("Both x and y are greater than 5")
    else:
        print("x is greater than 5, but y is not")

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# For loop with else statement
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

# Nested while loop
i = 0
while i < 5:
    j = 0
    while j < 3:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1

# Switch statement (not supported in Python)

# Ternary operator (also known as conditional expressions)
result = "Greater" if 5 > 3 else "Less"
print(result)