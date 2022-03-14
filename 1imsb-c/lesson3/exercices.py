# -------------
# Recap variables
# -------------
# firstname = "Collin"
# familyname = "Van der Vorst"
# fullname = firstname + " " + familyname
# age = 30
# length = 1.94
# isAwesome = True

# -------------
# Recap input + recap convert + recap output
# -------------
# firstname = input("Give me your firstname")
# age = int(input("Give me your age"))

# print(firstname + " is " + str(age) + " years old")
# print(firstname, "is", age, " years old")



# -------------
# Recap if
# -------------
# Booze Game
# < 16 only non-alocoholic
# < 18 only beer and soft drinks
# > 18 alles

# O: What is your age?
# I: 15
# O: HAHA NOT ALLOWED TO DRINK

# O: What is your age?
# I: 17
# O: DRINK THEM BEER

# O: What is your age?
# I: 20
# O: DRINK WHATEVER YOU WANT

# age = int(input("What is your age?"))

# if age < 16:
#     print("HAHA NOT ALLOWED TO DRINK")
# elif age < 18:
#     print("Only beer")
# else:
#     print("All drink")



# -------------
# Recap arithmetic
# -------------
# x = 5

# x+=1
# x = x + 1





# -------------
# Recap loops (range, string, for, while)
# -------------
# for x in range(0, 11):
#     print(x)
# print("End game")

# i = 0 
# for letter in "collin":
#     i += 1
#     print(letter)


# FOR: fibonacci
# I: How many numbers do you want? 5
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946
# numbers = int(input("How many numbers do you want?"))

# prevNumber = 0
# nextNumber = 1

# result = "0,1,"

# for number in range(0, numbers - 2):
#     # calculate sum
#     sum = prevNumber + nextNumber

#     # store value in prevNumber + next Number
#     prevNumber = nextNumber
#     nextNumber = sum

#     # concat new result
#     result += str(sum)
#     if (number != numbers - 3):
#         result +=","

# print(result)







# while Recap and and or
# username: collin
# password: 123

# O: give me your username:
# I: collin
# O: give me your password:
# I: collin
# O: YOU CAN NOT ENTER

# O: give me your username:
# I: collin
# O: give me your password:
# I: 123
# O: YOU CAN ENTER

# and -> all expressions should be true
# or -> at least 1 expressions should be true
# user = "collin"
# password = "123"

# inputUser = input("give me your username:")
# inputPass = input("give me your password:")

# while inputUser != user or inputPass != password:
#     print("YOU CAN NOT ENTER")

#     inputUser = input("give me your username:")
#     inputPass = input("give me your password:")

# print("YOU CAN ENTER")



# -------------
# Functions
# # -------------
# def exponent(grondgetal, exponent):
#     return grondgetal ** exponent

# print(exponent(5,2))
# print(exponent(5,3))


# -------------
# Recap list/tuple/set/dictionairy
# -------------
# student = [10, 12, 14]
# student.append(15)
# print(student)
# print(len(student))

# index = 0
# for grade in student:
#     print(grade)
#     index += 1


# for index in range(0, len(student)):
#     print(student[index])

# print(student)
# student.pop(1)
# print(student)

# kwartaal1 = [1000, 2000, 1000]
# kwartaal2 = [100, 200, 1000]
# kwartaal3 = [1030, 200, 1000]
# kwartaal4 = [100, 200, 1030]
# jaar = kwartaal1 + kwartaal2 + kwartaal3 + kwartaal4

# print(100 in jaar)

# user = {
#     "username" : "collin",
#     "password" : "123",
# }

# print(user["username"])





# -------------
# Student 1: 16, 14, 12
# Student 2: 12, 14, 12
# Student 3: 10, 11, 14
#
# O: student 1: 14.0
# O: student 2: 12.6666667
# O: student 3: 11.6666667
#
# O: test 1: 12.66666666667
# O: test 2: 13
# O: test 3: 12.66666666667
# -------------
student1 = [16, 14, 12]
student2 = [12, 14, 12]
student3 = [10, 11, 14]
gradebook = [
    student1,
    student2,
    student3
]

# average student
# index = 0
# for student in gradebook:
#     total = 0
#     index += 1

#     for grade in student:
#         total += grade

#     average = total / len(student)
#     print("Student", index,":",average)

# #average per test 
# countOfTest = len(gradebook[0])

# for index in range(0, countOfTest):
#     total = 0

#     for student in gradebook:
#         total += student[index]

#     average = total / len(gradebook)
#     print("Test", index,":",average)

# -------------
# Numpy Arrays
# -------------
import numpy as np # import package

# list = [4, 5, 6, 7]
# array = np.array([4, 5, 6, 7])

# print(list * 2) # [4, 5, 6, 7, 4, 5, 6, 7]
# print(array * 2) # [8, 10, 12, 14]

# omzetKwartaal1 = np.array([3000, 4000, 5000])
# omzetKwartaal1InclBtw = omzetKwartaal1 * 1.21
# print(omzetKwartaal1InclBtw)

# kostenKwartaal1 = np.array([1500, 700, 0])

# winstKwartaal1 = omzetKwartaal1InclBtw - kostenKwartaal1
# print(winstKwartaal1)
# print(winstKwartaal1 > 2500)
# print(np.where(winstKwartaal1 > 2500))


# print(winstKwartaal1)
# print(np.where(winstKwartaal1 > 2500, winstKwartaal1, winstKwartaal1 - 1 ))

# student1 = [16, 14, 12]
# student2 = [12, 14, 12]
# student3 = [10, 11, 14]

# gradebook = np.array([
#     [16, 14, 12],
#     [12, 14, 12],
#     [10, 11, 14]
# ])

# print(gradebook.sum(axis=1) / len(gradebook))
# print(gradebook.sum(axis=0) / len(gradebook))

# boekhouding = [ 1000, 2000, 3000, 500, 600, 800, 400, 250, 100, 100, 1000, 5000]
# boekhoudingNp = np.array(boekhouding)
# boekhoudingPerKwartaal = np.reshape(boekhoudingNp, (4, 3))
# print(boekhoudingPerKwartaal.sum(axis=1) * 1.21)

# list = np.arange(12)
# print(list)

# print(np.random.random((1,4)) * 100)
# print(np.random.random_integers(0, 60, (0,10)))

# list = np.array([4, 5, 6,])
# print(type(list))
# print(list.dtype)
# listFloat = list.astype('str')
# print(listFloat)
# print(listFloat.dtype)

# np.random.random => hoe geen 2d array krijgen 
# np.sum, wat als niet gelijke list in 2d array


list = np.arange(10)
print(list)

print(list[:2])
print(list[2:])
print(list[2:5])
print(list[::-1])

list = np.array([5, 10, 4, 11,1])
print(np.sort(list))
# -------------
# Dynamic numpy
# -------------





# -------------
# O: Create commandos [STOP] [ADD] [CHECK TODO] [LIST CHECK] [LIST UNCHECKED]

# I: ADD
# O: Add a todo:
# I: clean my room
# O: to do added

# I: LIST UNCHECKED
# O: 0. Learn python

# I: CHECK TODO
# O: 0
# I: Clean my room has been moved to checked

# I: LIST UNCHECKED
# O: 0. Learn python

# I: LIST CHECKED
# O: 0. Clean my room
# -------------
import math
a = -8
b = -1
c = -9
d = 5

result = math.sqrt(((a - b ) ** 2) + ((c - d) ** 2))
print(result)