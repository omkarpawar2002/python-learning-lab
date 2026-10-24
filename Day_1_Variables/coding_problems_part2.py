"""
QUESTION 26

Create variables for:
- name
- age
- roll_number
- marks
- city

Print each variable together with its type.
"""

name = "Ashok"
age = 23
roll_number = 101
marks = 78
city = "Pune"
print("Name        :", name, type(name))
print("Age         :", age, type(age))
print("Roll Number :", roll_number, type(roll_number))
print("Marks       :", marks, type(marks))
print("City        :", city, type(city))


"""
QUESTION 27

Create a variable named `data`.

Assign these values to it one after another:
1. Integer
2. String
3. Floating-point value
4. Boolean

After every assignment, print its value and type.
"""
data = 101
print(data, type(data))
data = "Information"
print(data, type(data))
data = 78.23
print(data, type(data))
data = False
print(data, type(data))


"""
QUESTION 28

Create:

a = 50
b = a
c = b

Print:
- values
- types
- IDs

for all three variables.

Investigate how several names can refer to the same object.
"""
a = 50
b = a
c = b
print(a, type(a), id(a))
print(b, type(b), id(b))
print(c, type(c), id(c))


"""
QUESTION 29

Create:
- a
- b

Make b refer to the object referenced by a.

Then reassign a to another value.

Display both variables afterward.

Demonstrate that reassigning one name does not
automatically reassign another name.
"""
a = 100
b = a
a = 50
print(a)
print(b)


"""
QUESTION 30

Create a list containing three values.

Assign the same list to a second variable.

Use an appropriate list operation to modify the list.

Then print both variables.

Observe shared references to a mutable object.
"""
li = [10, 20, 30]
new_li = li
li.append(101)
print(li)
print(new_li)


"""
QUESTION 31

Create a mutable object and assign it to two variables.

Print both IDs.

Modify the object's contents.

Print both IDs again.

Observe what happens to object identity when
the object is mutated.
"""
li = [10, 11, 12]
new_li = li
print(id(li))
print(id(new_li))
li.append(101)
print(id(li))
print(id(new_li))
# After modifying it will change the content itself between both because they both sharing same refferences.


"""
QUESTION 32

Create an integer and assign its reference
to a second variable.

Reassign the first variable.

Print both variables and their IDs.

Contrast reassignment with mutation.
"""
num = 101
num1 = num
num = 201
print(num, id(num))
print(num1, id(num1))


"""
QUESTION 33

Write a program that stores information
about an employee.

Requirements:
- Use at least five variables.
- All names should follow snake_case.
- Avoid one-letter names unless appropriate.
- Include at least one constant.
"""
emp_name = "Ketan"
emp_id = 1001
emp_salary = 25000
designation = "UI developer"
COMPANY_NAME = "Wipro"
print("Employee Name :", emp_name)
print("Employee Id :", emp_id)
print("Employee Salary :", emp_salary)
print("Designation :", designation)
print("Company Name :", COMPANY_NAME)


"""
QUESTION 34

Rewrite this code according to PEP 8 naming
and spacing principles:

studentName="Alex"
student_age=20
MAXmarks=500
totalMarks = 450

Then print the corrected variables.
"""
student_name = "Alex"
student_age = 20
MAX_MARKS = 500
total_marks = 450
print("Student Name :", student_name)
print("Student Age  :", student_age)
print("Max Marks    :", MAX_MARKS)
print("Total Marks  :", total_marks)


"""
QUESTION 35

Create variables for:
- customer's first name
- customer's account balance
- customer's account number
- maximum withdrawal amount
- minimum account balance

Use appropriate Python naming conventions.

Identify which names should be treated as constants
based on their meaning.
"""
first_name = "Kirti"
account_balance = 12500
account_number = 123412341234
maximum_withdrawl_amount = 11500
MINIMUM_ACCOUNT_BALANCE = 1000
