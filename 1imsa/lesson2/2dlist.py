gradebook = [
    [
        16, 8, 14, 15 #student 1
    ],
    [
        15, 14, 15, 14 #student 2
    ]
 ]


# AVERAGE PER STUDENT

# O: student 1: 13.25
# O: student 2: 14.5
# O: total average = 13,875

def average(list):
    total = 0

    for result in list:
        total+=result

    return total / len(list)

# array met alle gemiddeldes
studentAverages = []

#bereken het gemiddelde
for studentResults in gradebook:
    averageResult = average(studentResults)
    print(averageResult)

    # student gemiddelde toevoegen aan de grote array
    studentAverages.append(averageResult)

print(average(studentAverages))