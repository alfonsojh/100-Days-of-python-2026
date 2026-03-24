print('''---------------------------------------.--------
|                                       |         |
|    ,-----------------------------.    |    .    |
|    |                             |    |    |    |
|    |    ,-------------------.    |    |    |    |
|    |    |                   |    |    |    |    |
|    |    `----     ,----     |    |    |    |    |
|    |              | X       |    |    |    |    |
|    |    ,---------"---------:    |    `----'    |
|    |    |                   |    |              |
|    `----:    ,---------.    |    `---------.    |
|         |    |         |    |              |    |
|    .    |    |    .    |    |     ---------'    |
|    |    |    |    |    |    |                   |
:----'    |    |    |    |    |    ,--------------:
|         |    |    |    |    |    |              |
|    .    |    `----'    |    |    |     ----.    |
|    |    |              |    |    |         |    |
|    `----"---------     |    |    `---------'    |
|                        |    |                   |
`------------------------'    `--------------------''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

choice1 = (input('You are at a crossroad, where do you want to go? Type: "Left or Right" \n')).lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake '
          'there is an island in the middle of the lake '
          'Type "wait" to wait for a boat '
          'type "swim" to swim across the lake\n').lower()
    if choice2 == "wait":
        choice3 = input('You\'ve arrived at the island unharmed '
                        'there is a house with 3 doors , one red '
                        'one yellow and one blue '
                        'Which colour do you choose?\n').lower()
        if choice3 == "red":
            print("its a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You fond the treasure. YOU WIN!!!")
        elif choice3 == "blue":
            print("You enter in a room of beasts. Game Over")
        else:
            print("You enter a wrong colorr")
    else:
        choice4 = input('You\'ve got attacked by angry trout. Game Over')

else:
    choice3 = input('You\'ve fell in to a hole. Game Over')






