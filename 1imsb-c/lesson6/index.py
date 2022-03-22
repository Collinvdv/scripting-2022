# # Remove non - alpha chars
# def isChar(char):
#     ascciValue = ord(char)

#     if (ascciValue >= 48 and ascciValue <= 57) or (ascciValue >= 65 and ascciValue <= 90) or (ascciValue >= 97 and ascciValue <= 122):
#         return True

#     # non alpahnumeric
#     return False

# # matrix
# dimensions = input("Give me x and y:").split() # fe: 7 3 => ['7', '3']
# rows = int(dimensions[0]) # fe: 7
# columns = int(dimensions[1]) # fe: 3

# # Opvullen
# phrases = []
# for rowIndex in range(0, rows):
#     phrases.append(input())

# # Build the phrase 
# # phrases = ['thi', 'h%x', 'i #']
# phrase = ""
# for columnIndex in range(0, columns):
#     for rowIndex in range(0, rows):
#         word = phrases[rowIndex] # 'thi'
#         phrase += word[columnIndex]

# #phrase = This$#is% Matrix#  %!

# finalResult = ""
# prevCharIsChar = False

# for char in phrase:
#     if (isChar(char)):
#         finalResult += char
#     else:
#         if prevCharIsChar:
#             finalResult += " "

#     # save the previous char for the next loop
#     prevCharIsChar = isChar(char)

# import json
# import requests



# jsonFile = open("user.json")
# # json.load -> file
# # json.loads -> string
# userObject = json.load(jsonFile)

# for beer in userObject["favoriteBiertjes"]:
#     print(beer)


# car = {
#     "merk" : "ford",
#     "type" : "mustang"
# }

# # carString = json.dumps(car)
# # print(carString)
# # print(type(carString))

# carFile = open("car.json", "w") # w = overwrite, a = append, r = read

# json.dump(car, carFile)

# carFile.close()
# # json.dumps(dict) => dictionary naar een string

# jsonFile.close()

import requests, json

# response = requests.get("https://api.kanye.rest/")

# statusCode = response.status_code

# if statusCode == 200:
#     print("Api call is gelukt")
#     body = response.text
#     quoteObject = json.loads(body) # {"quote":"I need an army of angels to cover me while I pull this sword out of the stone"}
#     print(quoteObject["quote"])

quotes = []

# 10 unieke quotes
while len(quotes) != 10: 
    response = requests.get("https://api.kanye.rest/")
    quoteObject = json.loads(response.text)
    quote = quoteObject["quote"]

    if quote not in quotes:
        quotes.append(quote)

fileQuote = open("kanye-quotes.txt", "w")

for quote in quotes:
    fileQuote.write(quote + "\n")

fileQuote.close
