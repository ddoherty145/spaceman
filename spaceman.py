import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for  letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet


def is_guess_in_word(guess, secret_word):
    return guess in secret_word
    #TODO: check if the letter guess is in the secret word




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    print("Welcome to Spaceman!")
    print("Dave the Spaceman is running out of air to save him you need to guess the secret word.")
    print(f"The secret word has {len(secret_word)} letters.")
    print("You can guess one letter at a time.")
    print("You have a total of 7 incorrect guesses before Dave the Spaceman DIES!!\n")


    letters_guessed = []
    attempts_left = 7

    while attempts_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        print(f"Secret word: {get_guessed_word(secret_word, letters_guessed)}")
        print(f"Attempts left: {attempts_left}")
        print(f"Letters guessed so far: {', '.join(letters_guessed)}")

        guess = input("\nGuess a Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter or else Dave will be in trouble.\n")
            continue

        if guess in letters_guessed:
            print(f"You already guessed the letter '{guess}'. Try again.\n")
            continue

        
        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            print(f"Good guess! The letter '{guess}' is in the word. Dave is one step closer to being saved!\n")
        else:
            print(f"Oh No! The letter '{guess}' is incorrect, Dave is running out of air!\n")
            attempts_left -= 1

    if is_word_guessed(secret_word, letters_guessed):
        print(f"Congratulations! you've guessed the secret word '{secret_word}' correctly. YOU SAVED DAVE!")
    else:
        print(f"Sorry, you ran out of attempts. The secret word was '{secret_word}'. Dave ran out of air!")

    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
