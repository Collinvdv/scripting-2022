#  THE SAUSAGES
# price of 1kg sausages: 5.5EURO

# O: HELLO PERSON, HOW MANY KG SAUSAGES DO YOU WANT?
# I: 3
# O: Here is 3kg sausages for 16.5 euros. Give me your money!
# I: 15
# O: That is not enough! Give me your money!
# I: 20
# O: Here you go 3.5 euros back

# constant
priceSausage = 5.5

kgSausage = float(input("HELLO PERSON, HOW MANY KG SAUSAGES DO YOU WANT?"))
totalPrice = kgSausage * priceSausage

print("Here is ",kgSausage,"kg sausages for ",totalPrice," euros. Give me your money!")

owedMoney = float(input("Give me your money"))

while owedMoney < totalPrice:
    print("ja dat is te weinig");
    owedMoney = float(input("Give me your money"))

change = owedMoney - totalPrice

if change == 0:
    print("hier zijn de worsten")
else:
    print("Here you go ", change, "euros back")