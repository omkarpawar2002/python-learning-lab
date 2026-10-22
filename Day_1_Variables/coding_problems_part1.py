"""
QUESTION 1

Create a variable named `name` and assign your name to it.
Store your name as a string.
Print the variable.
"""

name = "kirti"
print("Name :", name)


"""
QUESTION 2

Create a variable called `age` and store an integer representing your age.
Print the value.
"""
age = 25
print("Age :", age)


"""
QUESTION 3

Create three variables:
- name
- age
- city

Store appropriate values and print all three.
"""
name = "Achind"
age = 20
city = "Mumbai"
print("Name :", name)
print("Age  :", age)
print("City :", city)


"""
QUESTION 4

Create variables for:
- student_name
- student_age
- student_marks

Print each variable on a separate line.
"""
student_name = "Arvind"
student_age = 18
student_marks = 89
print("Student Name :", student_name)
print("Student Age  :", student_age)
print("Student Marks :", student_marks)


"""
QUESTION 5

Create a variable containing a person's name.
Use type() to print its type.
"""
person_name = "Ravi"
print("Type :", type(person_name))


"""
QUESTION 6

Create a variable containing an integer.
Use type() to inspect it.
"""
number = 45
print("Type :", type(number))


"""
QUESTION 7

Create:
- name
- age
- height

Use type() on all three variables.
"""
name = "Chetan"
age = 23
height = 5.8
print("Name Type :", type(name))
print("Age Type :", type(age))
print("Height Type :", type(height))


"""
QUESTION 8

Create a constant named MAX_SCORE.

Requirements:
- Follow the uppercase naming convention.

Assign an appropriate value and print it.
"""
MAX_SCORE = 100
print(MAX_SCORE)


"""
QUESTION 9

Write a short program containing:
- one variable
- one useful comment
- one print() statement

The comment should explain something meaningful about the program.
"""
# Maximum Allowed Users
MAX_USERS = 100
print("Max Users :", MAX_USERS)


"""
QUESTION 10

Create a small Python program that begins with a documentation string.

The documentation string should describe what the program is intended to store.

Then create at least two variables.
"""
""" Demonstrate The Student Result """
first_name = "Keshav"
marks = 89
print("First Name :", first_name)
print("Marks :", marks)


"""
QUESTION 11

Create:
- first_name
- last_name

Assign values and print both.

Use proper Python naming conventions.
"""
first_name = "Chetana"
last_name = "Bhoir"
print("First Name :", first_name)
print("Last Name :", last_name)


"""
QUESTION 12

Create variables for:
- name
- age
- city
- country

Print each variable.

Requirements:
- Use snake_case.
- Do not use unnecessary abbreviations.
"""
name = "Anuj"
age = 21
city = "Pune"
country = "India"
print("Name    :", name)
print("Age     :", age)
print("City    :", city)
print("Country :", country)


"""
QUESTION 13

Create:

score = 50

Print it.

Then change the variable to 100 and print it again.
"""
score = 50
print("Score :", score)
score = 100
print("Score :", score)


"""
QUESTION 14

Create a variable called `value`.

First assign an integer to it.
Then assign a string to the same variable.

Use type() after each assignment.
"""
value = 100
print(type(value))
value = "data"
print(type(value))


"""
QUESTION 15

Create three variables:
- name
- age
- city

Assign all three using a single multiple-assignment statement.

Then print them.
"""
name, age, city = "Vedant", 19, "Satara"
print("Name :", name)
print("Age  :", age)
print("City :", city)


"""
QUESTION 16

Create:
- x
- y
- z

Assign the same value to all three using a single assignment statement.

Print all three.
"""
x = y = z = 100
print(x, y, z)


"""
QUESTION 17

Create:

a = 10
b = 20

Swap their values using Python's multiple-assignment syntax.

Print both after the swap.
"""
a = 10
b = 20
print("A :", a)
print("B :", b)
a, b = b, a
print("A :", a)
print("B :", b)


"""
QUESTION 18

Create:
- a
- b
- c

Assign different values.

Rotate their values so that:
- a receives b's original value
- b receives c's original value
- c receives a's original value

Use multiple assignment.
"""
a, b, c = 10, 11, 12
print("A :", a)
print("B :", b)
print("C :", c)
a, b, c = b, c, a
print("A :", a)
print("B :", b)
print("C :", c)


"""
QUESTION 19

Create:

x = 100

Print:
- x
- type(x)
- id(x)
"""
x = 100
print(x)
print(type(x))
print(id(x))


"""
QUESTION 20

Create:

x = 100
y = x

Print:
- id(x)
- id(y)

Investigate whether both names refer to the same object.
"""
x = 100
y = x
print(id(x))
print(id(y))


"""
QUESTION 21

Create:
- x
- y

Make both refer to the same value.

Then reassign x to another value.

Print:
- x
- y
- id(x)
- id(y)

Observe the difference between reassignment and shared references.
"""
x = 100
y = x
x = 50
print(x)
print(y)
print(id(x))
print(id(y))


"""
QUESTION 22

Create constants representing:
- maximum score
- minimum passing score
- number of months in a year

Follow uppercase naming conventions.

Print them.
"""
MAX_SCORE = 100
MIN_SCORE = 40
NUMBER_OF_MONTH_IN_YEAR = 12
print("Maximum Score :", MAX_SCORE)
print("Minimum Score :", MIN_SCORE)
print("Number Of Month :", NUMBER_OF_MONTH_IN_YEAR)


"""
QUESTION 23

Rewrite these invalid or poor variable names into valid,
readable Python identifiers:

- 1student
- student name
- class
- studentMarks
- x

Then create variables using your corrected names.
"""
student_1 = 101
student_name = "Kumar"
student_class = "A"
student_marks = 78
student_id = 1


"""
QUESTION 24

Create variables for:
- city name
- current temperature
- maximum temperature
- minimum temperature

Print all values.

Use appropriate naming conventions.
"""
city_name = "Mumbai"
current_temp = 28
max_temp = 40
min_temp = 12
print("City Name :", city_name)
print("Current Temperature :", current_temp, "degree celsius.")
print("Maximum Temperature :", max_temp, "degree celsius.")
print("Minimum Temperature :", min_temp, "degree celsius.")


"""
QUESTION 25

Create variables for:
- product name
- product price
- product quantity
- product code

Print each value and its type.
"""
product_name = "Laptop"
product_price = 80000
product_quantity = 10
product_code = "LAP#42190"
print("Product Name :", product_name, type(product_name))
print("Product Price :", product_price, type(product_price))
print("Product Quantity :", product_quantity, type(product_quantity))
print("Product Code :", product_code, type(product_code))