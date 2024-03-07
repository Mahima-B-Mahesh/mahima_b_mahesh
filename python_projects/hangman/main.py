import hangman_words
import hangman_arts
from replit import clear

import random


chosen_word = random.choice(hangman_words.word_list)
print(hangman_arts.logo)

display = []
word_length = len(chosen_word)

lives = 6

for _ in range(word_length):
    display += "_"


end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} not in the word. You lose a life. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
            print(f"The word is {chosen_word}")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(hangman_arts.stages[lives])
