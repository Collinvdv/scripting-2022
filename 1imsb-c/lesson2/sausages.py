#  THE SAUSAGES
# price of 1kg sausages: 5.5EURO

# O: HELLO PERSON, HOW MANY KG SAUSAGES DO YOU WANT?
# I: 3
# O: Here is 3kg sausages for 16.5 euros. Give me your money!
# I: 15
# O: That is not enough! Give me your money!
# I: 20
# O: Here you go 3.5 euros back
priceSausages = 5.5
sausagesOrder = float(input("HELLO PERSON, HOW MANY KG SAUSAGES DO YOU WANT?"))
totalPrice = priceSausages * sausagesOrder

givenMoney = float(input("Here is " + str(sausagesOrder) + "kg sausages for " + str(totalPrice) +" euros. Give me your money!"))

while givenMoney < totalPrice:
    givenMoney = float(input("That is not enough! Give me your money!"))

if givenMoney == totalPrice:
    print("Here are your sausages")
else:
    print ("Here are your sausages and " + str(givenMoney - totalPrice) +"euros back")