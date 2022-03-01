firstname = input("Give me your firstname")
lastname = input("Give me your lastname")
age = int(input("Give me your age")) # "30"
fullname = firstname + " " + lastname
height = 1.93
print(height)
print(type(height))
phrase = fullname + " is " + str(age) + " jaar oud"

# I: JEAN, VDV, 30
# O: YOU CAN ENTER

# I: LOLA, Zwarte, 15
# O: YOU CAN NOT ENTER, 2 YOUNG

# I: Pierre, Vdv, 70
# O: YOU CAN NOT ENTER, 2 OLD

# SOLUTION 1
if age < 18:
    print("You can not enter, 2 young")
elif age > 65:
    print("You can not enter, 2 old")
else:
    print("You can enter")

# SOLUTION 2
if age < 18 or age > 65:
    # you can not enter
    if age < 18:
        print("2 young")
    else:
        print("2 old")
else:
    print("you can enter")

# print(phrase)
# print(firstname + " " + lastname, "is", age, "jaar oud")