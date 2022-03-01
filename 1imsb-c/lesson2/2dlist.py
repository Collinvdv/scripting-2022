gradebook = [
    [ 18, 20, 10, 14 ], # student1
    [ 10, 10, 10, 10] # student2
]

print(gradebook[1][0])

# GIVE ME AVERAGE FOR EVERY STUDENT
# STUDENT 1: 15.5
# STUDENT 2: 10
# GIVE ME A TOTAL AVERAGE
# TOTAL AVERAGE: 12.75

def averageOfList(list):
    totalPoints = 0

    for points in list:
        totalPoints += points

    average = totalPoints / len(list)

    return average



studentIndex = 0
studentAverages = []

# Student berekenen
for studentGrades in gradebook:
    studentIndex += 1

    studentAverage = averageOfList(studentGrades)

    print("STUDENT", studentIndex, ":", studentAverage)
    studentAverages.append(studentAverage)

# Total berekenen
totalAverage = averageOfList(studentAverages)
print(totalAverage)