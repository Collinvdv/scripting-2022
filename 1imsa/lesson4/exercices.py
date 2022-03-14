#  Multiplication table

#  O : What number do you want to multiply?
#  I : 5
#  O : How many times?
#  I : 3
#  O : 0 x 5 = 0
#  O : 1 x 5 = 5
#  O : 2 x 5 = 10
# number = int(input("What number do you want to multiply?"))
# manyTimes = int(input("How many times?"))

# for x in range (0, manyTimes):
#     print(x, "x", number, "=", x * number )

























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
# commando = input ("add a number or say STOP to end and see result")
# sum = 0

# while commando != "stop":
#     number = int(commando)
#     sum += number
#     commando = input ("add a number or say STOP to end and see result")

# if sum < 0:
#     print("Your loss is " + abs(sum) + " euro")
# else:
#     print("Your profit is " + sum + " euro")































#  Calculate the sum of all numbers from 1 to a given number
#  For example,
#  if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

#  I: 10
#  O: 55

# input = int(input())
# result = 0

# for x in range(1, input + 1):
#     result += x

# print(result)















# Strings
# print("Collin \"The Awesome One\" Van der Vorst")
# print(r"Collin \"The Awesome One\" Van der Vorst")
# print("Collin \nVan der Vorst")

# phrase = "Python is mega leuk, juij "

# print(phrase[2:6])
# print(phrase[:6])
# print(phrase[6:])
# print(phrase[::-1])
	
# print(phrase[1::2]) # COLLIN WAT IS DIT? EXPLAIN ME :'(


# print(phrase.split())
# print(phrase.split(","))

# print("---".join("collin van der vorst".split()))

# name = "Collin 69 Van der Vorst"

# name = name.replace("69", "70")

# print(name)

# for letter in name:
#     print(letter)
#     print(letter.islower())
#     print(letter.isdigit())
#     print(letter.isspace())

# letter = input("Give me a letter")
# asciiNumber = ord(letter)

# print(letter + " is in ascii:" + str(asciiNumber))
# number = int(input("give me a number"))
# letter = chr(number)
# print(letter)












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





# character = input()
# asciiCharacter = ord(character) #r = 114

# result = ""

# if character.islower():
#     for x in range (asciiCharacter + 1, 123):
#         result += chr(x) + " "
# else:
#     if character.isupper():
#         for x in range (asciiCharacter + 1, 90):
#             result += chr(x) + " "
#     else:
#         result ="ONLY LETTERS"

# print(result)


import re

string = "4 Vandaag is het 7 graden, morgen is het 11 graden en overmorgen 16 graden"
string = "product a is 7USD, product b is 8USD"
weerValidation = re.compile("USD")
result = weerValidation.sub(" dollar", string)

print(result)

# result = re.search(r"\d", string) # search -> geeft 1 resultaat terug 
# print(result)
# print("First occurence = " + result.group())

# result = re.findall(r"\d+", string)
# print(result)

# mail = input()
# mail2 = input()


# mailValidationRegex = re.compile(r"[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]")
# mailValidationRegex.search(mail)
# mailValidationRegex.search(mail2)

