#  Multiplication table

#  O : What number do you want to multiply?
#  I : 5
#  O : How many times?
#  I : 3
#  O : 0 x 5 = 0
#  O : 1 x 5 = 5
#  O : 2 x 5 = 10
# number = int(input(" What number do you want to multiply?"))
# howManyTimes = int(input("How many times?"))

# for x in range(0, howManyTimes):
#     print(x," x ", number, " =", x * number)

























#  Accountancy application

#  O: add a number or say STOP to end and see result
#  I: 100
#  I: 50
#  I: 250
#  I: -100
#  I: -200
#  I: STOP
#  O: Your profit is 100 euro

#  O: add a number or say STOP to end and see result
#  I: 100
#  I: 50
#  I: 250
#  I: -100
#  I: -400
#  I: STOP
#  O: Your loss is 100 euro

# print("add a number or say STOP to end and see result")
# commando = input()
# result = 0

# while commando != "stop":
#     result += int(commando)
#     commando = input()

# if (result < 0):
#     print("Your loss is",abs(result), "euro")
# else:
#     print("Your profit is",abs(result), "euro")

































#  Calculate the sum of all numbers from 1 to a given number
#  For example,
#  if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

#  I: 10
#  O: 55
# number = int(input())
# result = 0

# for x in range(1, number + 1):
#     result += x

# print(result)


# print("Collin Van der Vorst")
# print(r"Collin \"The awesome Teacher\" \n\tVan \\ der Vorst")

# fullname = "Collin Van der Vorst"
# print(fullname[0:2]) #Co
# print(fullname[:2]) #Co
# print(fullname[2:]) #llin Van der Vorst
# print(fullname[::-1]) #tsroV red naV nilloC
# print(fullname[1::2])
# print("Collin" in fullname)

# print(fullname.split()) #['Collin', 'Van', 'der', 'Vorst']
# print(fullname.split()[0]) #'Collin'
# print(fullname.split("n")) #['Colli', ' Va', ' der Vorst']
# print(fullname.split("in")) #['Colli', ' Va', ' der Vorst']

# slug = "all-info-on-strings-and-regex"
# print(" ".join(slug.split("-")))

# names = ["Collin", "Lisa", "Youssef"]
# phrase = " is verliefd op ".join(names)
# print(phrase)

# phrase = "Collin is 31 jaar en 194 cm"
# phrase.replace("Collin", "Colin")
# print(phrase)
# for character in phrase:
#     print("------------")
#     print(character)
#     print("Is lower:", character.islower())
#     print("Is upper:", character.isupper())
#     print("Is digit:", character.isdigit())
#     print("Is space:", character.isspace())


# character = input()
# print("the ascii value is", ord(character))

# number = int(input())
# print(number, " is equal to ", chr(number))






















# Ask a character
# Give them every character till z
#
# I: R
# O: S T U V W X Y Z
#
# I: r
# O: s t u v w x y z
#
# I: 7
# O: only letters
#
# def restOfAlphatbet(character,positionOfZ):
#     asciiCode = ord(character)
#     result = ""

#     for x in range(asciiCode + 1, positionOfZ):
#         result += chr(x) + " "

#     print(result)


# character = input()

# if character.islower():
#     restOfAlphatbet(character, 123)
# elif character.isupper():
#     restOfAlphatbet(character, 91)
# else:
#     print("only letters")


import re

phrase = "Collin is 31 jaar, 194 centimer en woont in Dendermonde"
phrase2 = "Lisa is 26 jaar, 160 centimeter en woont in Dendermonde"

compilerDigits = re.compile(r"\d")


print(re.search(r'\d',phrase))
print(re.findall(r'\d',phrase))

print(compilerDigits.findall(phrase))
print(compilerDigits.findall(phrase2))
# result = re.search(r'\d', phrase)
# print("First occurence = " + result.group())
# print("Location = " + str(result.span()))

# results = re.findall(r'\d', phrase)
# print(results)
