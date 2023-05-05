import random
import hangman_lives_stages
import hangman_word_list
   
#importing from hangman_lives_stages
stages = hangman_lives_stages.stages

#importing from hangman_word_list
word_list = hangman_word_list.word

chosen_word1 = random.choice(word_list)
chosen_word = chosen_word1.lower()
print(chosen_word)

lives = 6

display = []
for leters in range(len(chosen_word)):
    display += "_"
print(display)


end_of_game = False
while not end_of_game: 
    guess = input("Guess a letter: ").lower()
    print(guess)
    if guess in display:
        print(f"You've already guessed the letter {guess}.")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:
        print(f'{guess} is not in the word. You lose  a life.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
            
    print(f"{' '.join(display)}")
            
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])


































    












