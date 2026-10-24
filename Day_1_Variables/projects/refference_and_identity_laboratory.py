"""
PROJECT 4: REFERENCE & IDENTITY LABORATORY

Objective:
Investigate how Python variables refer to objects.

Your program should demonstrate:

1. Two names referring to the same object.
2. Printing their values.
3. Printing their types.
4. Printing their IDs using id().
5. Reassigning one variable.
6. Observing the effect of reassignment.
7. Creating a mutable object shared by two variables.
8. Modifying the mutable object.
9. Printing IDs before mutation.
10. Printing IDs after mutation.
11. Reassigning one variable to a new object.

Requirements:
- Organize the program into clearly labeled sections.
- Use comments to explain each experiment.
- Do not depend on specific numeric values returned by id().
- Make the output easy to understand.
"""

print("========================================")
print("=== REFERENCE & IDENTITY LABORATORY ====")
print("========================================")

name1 = "Ankit"
name2 = name1
print("Name 1 :", name1, type(name1), id(name1))
print("Name 2 :", name2, type(name2), id(name2))

print()

name1 = "Neha"
print("Name 1 :", name1, type(name1), id(name1))
print("Name 2 :", name2, type(name2), id(name2))

print()

li_1 = [11, 22, 33]
li_2 = li_1
# Before Mutation
print(li_1, id(li_1))
print(li_2, id(li_2))

print()

li_1.append(101)
# After Mutation
print(li_1, id(li_1))
print(li_2, id(li_2))

print()

li_1 = "Welcome"
print(li_1, id(li_1))
print(li_2, id(li_2))


print("========================================")
