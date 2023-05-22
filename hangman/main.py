# clear only works in replit
from replit import clear
import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)
print("\nWelcome! Let the game begin!\n")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear() # this only works in replit

    if guess in display:
        print(f"You've already guessed '{guess}'. Try again!")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print("Good guess!")

    if guess not in chosen_word:
        print(f"You entered '{guess}'. There is no such letter in the word, sorry. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Game over.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Congrats! You win.")

    print(stages[lives])