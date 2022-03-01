# print(range(0, 11))
# for x in range(0, 11):
#     print(x, " * 5 = ", x * 5)
#     print(str(x) + " * 5 = " + str(x * 5))

# firstname = "collin"
# for letter in firstname:
#     print(letter)


counter = 0
while counter <= 10:
    print(counter, " * 5 =", counter * 5)
    counter+=1


# ASK FOR A WORD, WHEN BANANA STOP, WHEN NOT BANANA ASK AGAIN

# O: GIVE ME A WORD
# I: COLLIN
# O: GIVE ME A WORD
# I: BANANA
# O: END GAME

word = input("GIVE ME A WORD")

while word.upper() != 'BANANA':
    word = input("GIVE ME A WORD")

    if word.upper() == 'BANANA':
        print("END GAME")