# O: GIVE ME A WORD
# I: apple
# O: WRONG

# O: GIVE ME A WORD
# I: peach
# O: WRONG

# O: GIVE ME A WORD
# I: banana
# O: END GAME

word = input("GIVE ME A WORD")

while word != "banana":
    print("WRONG")
    word = input("GIVE ME A WORD")

print("END GAME")