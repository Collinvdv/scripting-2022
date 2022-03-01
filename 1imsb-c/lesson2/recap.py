length = 1.93
print
firstname = input("Give me your firstname:")
familyname = "Van der Vorst"
age = int(input("Give me your age"))
isAwesome = True
# print(type(age)) -> get type of this instance

print(firstname + familyname + str(age) + "years old")

if age >= 18:
    print("You are an adult")
elif age < 16:
    print()
else:
    print("you are not an adult")

print("end program")

for i in range(0, 11):
    print(i)

commando = input("Give me a commando, say stop to stop")

while commando != "stop":
    commando = input("Give me a commando, say stop to stop")
