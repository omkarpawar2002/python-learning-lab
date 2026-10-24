"""
PROJECT 5: STUDENT RECORD PROTOTYPE

Objective:
Build a clean prototype of the data portion of a
student-management application using only todays concepts.

Store:
- student_name
- student_id
- age
- city
- course_name
- marks
- maximum_marks
- academic_year
- institution_name

Requirements:

1. Begin with a documentation string.
2. Use meaningful variable names.
3. Follow snake_case naming convention.
4. Use uppercase names for intended constants.
5. Use multiple assignment at least once.
6. Display all student information.
7. Use type() to inspect relevant values.
8. Use id() to demonstrate object identity.
9. Include useful comments.
10. Avoid unnecessary complexity.

"""

print("========================================")
print("====== STUDENT RECORD PROTOTYPE ========")
print("========================================")

student_name = "Kirti"
student_id = 101
age, city = 23, "Mumbai"
course_name = "Full Stack Python"
marks = 131
MAX_MARKS = 150
academic_year = 1
INSTITUTION_NAME = "codewithomi.tech"

print("Student Name   :", student_name)
print("Student Id     :", student_id)
print("Age            :", age)
print("City           :", city)
print("Course Name    :", course_name)
print("Marks          :", marks)
print("Max Marks      :", MAX_MARKS)
print("Academic year  :", academic_year)
print("Institute Name :", INSTITUTION_NAME)

print()
# Here We Check Type Of Each Object
print("Student Name   :", type(student_name))
print("Student Id     :", type(student_id))
print("Age            :", type(age))
print("City           :", type(city))
print("Course Name    :", type(course_name))
print("Marks          :", type(marks))
print("Max Marks      :", type(MAX_MARKS))
print("Academic year  :", type(academic_year))
print("Institute Name :", type(INSTITUTION_NAME))

student_name = "Kaushik"
age = 30
print()
# Here We Check Identity Of Each Object
print("Student Name   :", id(student_name))
print("Student Id     :", id(student_id))
print("Age            :", id(age))
print("City           :", id(city))
print("Course Name    :", id(course_name))
print("Marks          :", id(marks))
print("Max Marks      :", id(MAX_MARKS))
print("Academic year  :", id(academic_year))
print("Institute Name :", id(INSTITUTION_NAME))

new_academic_year = academic_year
print(id(academic_year))
print(id(new_academic_year))

print("========================================")
