import random
from hangmanWords import word_list
from  hangmanArt import stages , logo
# This is the classic Hangman


# TODO-1 - Randomly choose a word from the word_list and assign it ro a variable called chosen_word. Then print it.
#Create a variable called placeholder

lives = 6

print(logo)

chosen_word = random.choice(word_list)
#print(chosen_word)
placeholder =""
word_lenght = len(chosen_word)

for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Create a loop to let the user guess again
game_over = False

correct_letters = []
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT***************************************************")

    guess = input("Guess a letter: ").lower()
    print(guess)

    # TODO-3 - Check if the letter guessed (guess) is one of the letters in chosen_word. Print if "Right"  if it is,
    # Wrong if it's not.
    # Create a variable called display to write the guess letter in the right position and a _ in  the rest of the string
    # Change the for loop so that you keep the previous correct letters in display
    if guess in correct_letters:
        print(f"Letter already guessed {guess}")

    display =""
    for letter in chosen_word:
        if letter == guess:
            # print("Right")
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter

        else:
            #print("Wrong")
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -=1
        print(f"You guessed {guess}, is not in the word you loose a life.")

        if lives == 0:
            game_over = True

            print(f"*********************************You Lose! The word was {chosen_word}********************************")


    if "_" not in display:
        game_over = True
        print("********************************You win!********************************")

# TODO- Create an ascii art for hangman stages

    print (stages[lives])