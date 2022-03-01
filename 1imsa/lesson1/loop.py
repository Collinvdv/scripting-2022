# number = int(input("give me a number"))
# for x in range(10, 21):
#     print(x, " * ", number, " = ", number * x)
#     # print(str(x) + " * " + str(number) + " = " + str(number * x))
# print("end game")

# word = input("give me a random word")
# for letter in word:
#     print(letter)

number = int(input("give me a number"))
counter = 0

while counter <= 10:
    print(counter, " * ", number, " = ", number * counter)
    counter += 1