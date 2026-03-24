#Program for rock paper and scissors game

import random

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = '''   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''


game_images = [rock, paper, scissors]

user_choice = int(input('Rules: Enter "0" for rock , enter "1" for paper , enter "2" for scissors\n'))
if user_choice >= 0 and user_choice <= 2:
    print("user chose")
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("computer chose:")
print(game_images[computer_choice])

if user_choice >=  3 or user_choice < 0:
    print("Invalid Number game over")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice  > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif user_choice == computer_choice:
    print("its a draw!")









