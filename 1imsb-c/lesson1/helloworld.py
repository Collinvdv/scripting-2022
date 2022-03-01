# first variable
firstname = input("Give me your firstname:")
age = int(input("Give me your age:"))

# Print outputs to terminal, str() converts data to string, int()
# parse to int -> int()
# parse to string -> str()
# when print has to be full string, so convert ints
print(firstname + " is " + str(age) + " years old.")

# if condition : , do click on tab to get in the IF statement
if age < 18 or age > 65:
    print("2 young or 2 old")
else:
    print("You can enter the app")
