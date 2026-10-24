"""
PROJECT 2: STUDENT INFORMATION CARD

Objective:
Build a small student information program.

Store:
- student_name
- age
- roll_number
- city
- marks
- maximum_marks

Requirements:
- Use multiple assignment at least once.
- Create at least one constant.
- Display all information.
- Display the type of each value using type().
- Follow Python naming standards.
- Include a module-level documentation string.
"""

""" Build A Student Information Card Project """
print("========================================")
print("====== STUDENT INFORMATION CARD ========")
print("========================================")

student_name = "Ashvini"
age, roll_number = 23, 101
city = "Pune"
marks = 382
MAX_MARKS = 500

print("Student Name :", student_name)
print("Age          :", age)
print("Roll Number  :", roll_number)
print("City         :", city)
print("Marks        :", marks)
print("Max Marks    :", MAX_MARKS)

print()

print("Student Name Type :", type(student_name))
print("Age Type          :", type(age))
print("Roll Number Type  :", type(roll_number))
print("City Type         :", type(city))
print("Marks Type        :", type(marks))
print("Max Marks Type    :", type(MAX_MARKS))
print("========================================")
