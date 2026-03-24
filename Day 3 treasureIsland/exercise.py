#conditional to chec a number if is odd or even
#number=int (input("Please Enter a Number:\n"))

#if number % 2 == 0:
    #print(f"This number {number} is even")
#else: 
    #print(f"This number {number} is odd" )
#------------------------------------------------------------#
#if statements , elif statements , multiple  statements Nested Statement

#print("Welcome to roller Coaster")
#heigth = int(input("What is your heigth? "))
#bill = 0


#if heigth >= 120:
 #   print("You can ride the roller coaster")
  #  age = int(input("What is your age?"))
   # if age <=12:
    #    bill = 5
     #   print("Please pay 5")
    #elif age <=18:
    #    print("Please pay $7")
     #   bill = 7
   # else:
    #    print("Please pay $12")
     #   bill = 12
    #want_photo = input("Would you like to have a photo take? (y/n) ")
    #if want_photo == "y":
     #   bill += 3
    #print(f"Your final price is ${bill}")


#else:
 #   print("You cannot ride the roller coaster")

#__________________________________________________________________________________

print("Welcome to pizza Python")
bill = 0

size = str(input("What is your pizza size? S M or L? "))

if size == "S":
    bill += 15
    peperoni = str(input("Would you like extra peperonni ?  Y or N? "))
    if peperoni == "Y":
        bill += 2

elif size == "M":
    bill += 20
    peperoni = str(input("Would you like extra peperonni ?  Y or N? "))
    if peperoni == "Y":
        bill += 3

elif size == "L":
    bill += 25
    peperoni = str(input("Would you like extra peperonni ?  Y or N? "))
    if peperoni == "Y":
        bill += 3

else:
    print("invalid size")

    exit()

cheese = input("Would you like extra cheese? Y or N? ")
if cheese == "Y":
        bill += 1

print(f"Please pay ${bill}")


