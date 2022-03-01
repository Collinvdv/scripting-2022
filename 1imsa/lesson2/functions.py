def checkNegative(number):
    if number > 0:
        return "positive"
    elif number == 0:
        return "neutral"
    else:
        return "negative"

inputNumber = int(input("Give me your number"))
result = checkNegative(inputNumber)

print(result)