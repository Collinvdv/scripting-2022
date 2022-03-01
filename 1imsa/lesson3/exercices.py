# -------------
# Recap variables
# -------------
# firstname = "Collin"
# age = 30
# length = 1.93
# isMarried = False
# print(type(length))

# -------------
# Recap input + recap convert
# -------------
# firstname = input("Give me your firstname")
# age = int(input("Give me your age"))
# length = float(input("Give me your height"))


# -------------
# Recap output
# -------------
# print("Your firstname is " + firstname + " and your age is " + str(age))
# print("Your firstname is", firstname, "and your age is", age)
# phrase = "number is " + str(30)


# -------------
# Recap if
# -------------
# Booze Game
# < 16 only non-alocoholic
# < 21 only beer and soft drinks
# > 21 alles

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
# elif age < 21:
#     print("DRINK THEM BEER")
# else:
#     print("DRINK WHATEVER YOU WANT")





# -------------
# Recap arithmetic
# -------------





# -------------
# Recap loops (range, string, for, while)
# -------------

# FOR: fibonacci
# I: How many numbers do you want?
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

# YOU CAN 3 TIMES otherwise UNAUTHORIZED

# username = input("Give me your username:")
# password = input("Give me your password:")
# amountOfTries = 1

# while username != "collin" or password != "123":
#     print("you can not enter")

#     amountOfTries += 1

#     if amountOfTries > 3:
#         break

#     username = input("Give me your username:")
#     password = input("Give me your password:")

# if amountOfTries > 3:
#     print("UNAUTHORIZED")
# else:
#     print("you can enter")


# -------------
# Functions
# -------------
# def exponent(getal, exponent):
#     return getal**exponent


# def printExponent(getal,exponent):
#     print(exponent(5, 2))


# test1 = exponent(5, 2)
# print(test1)

# test2 = exponent(5, 3)
# print(test2)



# -------------
# Recap list/tuple/set/dictionairy
# -------------
# results = [10, 15, 20, "Collin", True, [1, 23] ] # []-> list
# results2 = [10, 8]

# results = results + results2

# # test.append(20)
# # test.pop(1)

# print(len(results))

# for result in results:
#     print(result)

# for index in range(0, len(results)):
#     print(index, results[index])

# user = {
#     "age": 30,
#     "username": "collindv",
#     "password": "collin"
# }

# users = [{
#     "age": 30,
#     "username": "collindv",
#     "password": "collin"
# }, {
#     "age": 30,
#     "username": "collindv2",
#     "password": "collin"
# }]

# print("Age of", user["username"], "is", user["age"])
# print(users)


# -------------
# Student 1: 16, 14, 12
# Student 2: 12, 14, 12
# Student 3: 10, 11, 14
#
# O: student 1: 14.0
# O: student 2: 12.6666667
# O: student 3: 11.6666667
#
#
# O: test 1: 12.66666666667
# O: test 2: 13
# O: test 3: 12.66666666667
# -------------
# gradebook = [
#     [ 16, 14, 12], #student1
#     [ 12, 14, 12], #student2
#     [ 10, 11, 14], #student3
# ]

# # per student gemiddelde berekenen
# for studentGrades in gradebook:
#     sum = 0
#     for grade in studentGrades:
#         sum += grade
#     print(sum / len(studentGrades))

# # per test gemiddele berekenen
# for testIndex in range(0, len(gradebook[0])):
#     sum = 0;
#     for studentGrades in gradebook:
#         sum += studentGrades[testIndex]
#     print(sum / len(gradebook[0]))



# -------------
# Numpy Arrays
# -------------
import numpy as np

# gradebook = np.array([
#     [ 16, 14, 12], #student1
#     [ 12, "14", 12], #student2
#     [ 10, 11, 14], #student3
# ])

# print(gradebook.sum(axis=0) / len(gradebook)) # test
# print(gradebook.sum(axis=1) / len(gradebook)) # students

# print(gradebook.min())
# # print(c)
# # c %= 3
# # print(c)

# jan, februari, maart
# omzet = np.array([1000, 4000, 3000])
# kosten = np.array([400, 0, 1600])
# winst = omzet - kosten

# print(winst)
# print(winst.sum())

# # 1euro = 1.57 
# winstDollar = winst * 1.50
# print(winstDollar)

# print(np.arange(50)) 



# list = 	np.random.random_integers(0, 100, (4,))
# list = np.array([4, 4.5])
# print(type(list))  
# print(list.dtype)


# winst = np.array([
#     100,
#     400,
#     400,
#     300,
#     200,
#     100,
#     400,
#     1000,
#     2000,
#     5000,
#     2000,
#     1000
# ])

# winstNaBelasting = np.where(winst >= 1000, winst * 1.1, winst )

# for winst in winstNaBelasting:
#     print(winst)

# # kwartaalWinst = np.reshape(winst, [4,3]).sum(axis=1)

# # print(kwartaalWinst)

# list = np.arange(8)


# -------------
# Gradebook Numpy
# -------------
# Student 1: 16, 14, 12
# Student 2: 12, 14, 12
# Student 3: 10, 11, 14



names = np.array(["Collin", "Collin Junior"])
fullnames = names + " Van der Vorst"
print(fullnames)



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