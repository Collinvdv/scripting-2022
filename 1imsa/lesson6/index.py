# #  01 The Matrix
# def isChar(character):
#     asciiChar = ord(character) # A -> 65
#     # ascii 48 and 57 OR 65 and 90 OR 97 and 122
#     if asciiChar >= 48 and asciiChar <= 57:
#         return True

#     if asciiChar >= 65 and asciiChar <= 90:
#         return True

#     if asciiChar >= 97 and asciiChar <= 122:
#         return True

#     return False

# dimensions = input().split() # 7 3 => ['7', '3']

# rows = int(dimensions[0])
# columns = int(dimensions[1])

# # Filling in the arrays
# inputWords = []
# for index in range(0, rows):
#     inputWords.append(input())

# # Concat one big string 
# output = ""
# for columnIndex in range(0, columns):
#     for rowIndex in range(0, rows):
#         output += inputWords[rowIndex][columnIndex]

# # This$#is% Matrix#  %!
# finalOutput = ""
# isPrevChar = ""

# for letterIndex in range(0, len(output)):
#     if isChar(output[letterIndex]):
#         finalOutput += output[letterIndex]
#     else:
#         if isPrevChar:
#             finalOutput += " "

#     # save prev char
#     isPrevChar = isChar(output[letterIndex])

# print(finalOutput.strip())

# JSON
import json

# load: file load
# loads: string load

# userFile = open("user.json")
# user = json.load(userFile) # plain text -> dictionary
# print(type(user))

# userText = json.dumps(user) # dictionary -> plain text
# print(type(userText))


# users = {}
# users["users"] = [ {
#     "username": "collinvdv",
#     "age": 30
# }, {
#     "username": "larsnolftv",
#     "age": 20
# } ]

# json_file = open('users.json', 'w') # w -> write, a -> append, r -> read 
# json.dump(users, json_file) # json.dump(dictionary, file)
# json.dumps(users) # json.dumps(dict) -> string
# json_file.write(json.dumps(users))
# # json_file.write()
# json_file.close()


# import requests

# quotes = []

# while len(quotes) != 10:
#     response = requests.get("https://api.kanye.rest/")
#     quote = response.text # plain text
#     #json.loads(quote) { quote : "you ..."}
#     quote = json.loads(quote) # plain text -> dictionry json.loads(str), json.load()
#     quote = quote["quote"]
#     print(quote) #You can't look at a glass half full or empty if it's overflowing. 

#     if quote not in quotes:
#         quotes.append(quote);

# file = open("quotes.txt", "w") 

# for quote in quotes:
#     file.write(quote + "\n")

# file.close()
# print(quotes)

text = input()
print(text)