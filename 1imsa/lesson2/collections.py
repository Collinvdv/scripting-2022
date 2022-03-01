# list -> []
students = ["Anouk", "Collin", "Ian"]

students[1] = "Colin"

students.append("Mo")

students = students + ["Kim"]

print(students)

students.pop(0)

print(students[0: 2])
# print(students[0])
# print(students[-1])
# print(len(students))

for student in students:
    print(student)

print(students)
for i in range(0, len(students)):
    print(i, ":", students[i])

print("Kim" in students)