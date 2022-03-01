#  AWESOME BANDNAME GENERATOR with 3 words
#  { "the", "a", "not", "all"} => give me 1 random item back
#  { } => give me 1 random item back
#  { } => give me 1 random item back
#  Command YES or ADD NEW  to add new band name, Command STOP to stop the game

#  O: Hello to my crazy band generator
#  O: You want to know a new band?
#  I: YES
#  O: the awesome jebus
#  O: You want to know a new band?
#  I: YES
#  O: not ugly pigeon
#  O: You want to know a new band?
#  I: STOP
#  O: BEY BEY

import random

def randomBandname():
    words1 = [ "the", "a", "not", "all" ]
    words2 = [ "ugly", "awesome", "nice", "perfect", "hardcore" ]
    words3 = [ "pigeon", "student", "bird", "flower", "jebus", "satan" ]

    return random.choice(words1) + " " + random.choice(words2) + " " + random.choice(words3)

print("Hello to my crazy band generator")

command = input("You want to know a new band?")

while command == "yes":
    print(randomBandname())

    command = input("You want to know a new band?")

print("BEY BEY")

