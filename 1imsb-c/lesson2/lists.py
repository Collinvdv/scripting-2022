students = ["Yasine", "Cedric", "Collin"]
students[0] = "Yassine"
students.append("Lisa")
students.pop(1)

students = students + ["John", "Kim"]

# print(students)
# print(students[0:2])
# print(students[-2])
# print(len(students))

for student in students:
    print(student)

for studentIndex in range(0, len(students)):
    print(studentIndex, students[studentIndex])
