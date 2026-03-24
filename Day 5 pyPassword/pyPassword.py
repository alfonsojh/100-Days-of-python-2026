# # This is a program to generate a safe password
# students_scores = [85, 120, 95, 60, 150, 175, 40, 200, 130, 110, 90, 70, 160, 180, 55, 100, 145, 155, 125, 80]
# total_exam_score = sum(students_scores)
# print(total_exam_score)
#
# sum = 0
# for score in students_scores:
#     sum += score
# print(sum)
#
# max_score = 0
#
# for score in students_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)
#
# total = 0
# for number  in range (1, 101):
#     total += number
#     print(total)
#
#
#================Password Generator#
import random

alphabet = [
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
]
numbers = ['1','2','3','4','5','6','7','8','9','10']
symbols = ["!","@","#","$","%","&","*","?","+","="]

print("This is a password Generator , please follow the instructions\n")
nr_alphabet=int(input("How many alphabet letter's do you want in your password? :\n"))
nr_number=int(input("How many number's do you want in your password? :\n"))
nr_symbol=int(input("How many symbol's do you want in your password? :\n"))

#easy level
# password = ""
# for char in range(0 , nr_alphabet):
#     password += random.choice(alphabet)
# for char in range(0 , nr_number):
#     password += random.choice(numbers)
# for char in range(0 , nr_symbol):
#     password += random.choice(symbols)
#
# print(password)

#hard level
password_list = []
for char in range(0 , nr_alphabet):
    password_list.append(random.choice(alphabet))
for char in range(0 , nr_number):
    password_list.append(random.choice(numbers))
for char in range(0 , nr_symbol):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is :{password}")
