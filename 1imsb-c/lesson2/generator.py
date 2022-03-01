#  AWESOME BANDNAME GENERATOR with 3 words
#  { "the", "a", "not", "all"} => give me 1 random item back
#  { "ugly", "awesome", "nice", "perfect", "hardcore"} => give me 1 random item back
#  { => give me 1 random item back
#  Command YES to add new band name, Command STOP to stop the game

#  O: Hello to my crazy band generator
#  O: You want to know a new band?
#  I: YES
#  O: the awesome jebus
#  O: You want to know a new band?
#  I: YES
#  O: not ugly pigeon
#  O: You want to know a new band?
#  I: STOP
#  O: BYE BYE

import random

def randomBandname():
    list1 = ["the", "a", "not", "all"]
    list2 = ["ugly", "awesome", "nice", "perfect", "hardcore"]
    list3 = ["pigeon", "student", "bird", "flower", "jebus", "satan"]

    return random.choice(list1) + " " + random.choice(list2) + " " + random.choice(list3)

print("Hello to my crazy band generator")

commando = input("You want to know a new band?")

while commando != "stop":
    print(randomBandname())
    commando = input("You want to know a new band?")
