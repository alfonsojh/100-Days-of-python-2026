
#print("Hello"[-3])
#Print types
#print(type("hello"))
#print(type(123))
#print(type(123.2))
#print(type(True))
#Exercise : Concatenate  string and text types str and int
#print("number of letters in your name: " + str(len(input("enter your name"))))
#print (3*3+3/3-3)

#age = 45
#name = "pedro"
#value = True
#print(f"your age is: {age}, your name is: {name}, and your value is: {value}")

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10% , 12%, or 15%?\n"))
people = int(input("How many people to split the bill?\n"))
# Using PEMDASLR
result = ((bill * (tip /100) + bill) / people)

print(f"Each person should pay: ${round(result,2)}")





