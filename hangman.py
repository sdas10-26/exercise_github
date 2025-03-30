import string

def display_word(word, guess):
    """
    Creates a string that represents the current state of the word the user is trying to guess
    Args:
        word(str): The word the user is trying to guess.
        guess(list): List of letters the user has guessed correctly.

    Returns:
        str: Returns a string that represents the word with the correctly guessed letters visible and unguessed letters are represented with dashes(-).

        """
    display = ""
    for letter in word:
        if letter in guess:
            display += letter
        else: 
            display += "-"
    return display


def hangman():
    """A very simple implementation of a classic game of Hangman. The player tries to guess the letters of a hidden word with a limited number of incorrect attempts permitted. 
    
    The game will end when the user had guessed the word correctly or when they have used all of the limited number of incorrect attempts permitted.
        """
    #List of the correctly guessed letters
    guessed_letter = []
    #The word the user is trying to guess
    word = "python"
    #Counter for incorrect guesses
    strikes = 0
    #Maximum number of incorrect guesses permitted
    max_strikes = 5
    print("Welcome to the Hangman Game!")
    #Main loop and will run while strikes is less than the max_strikes
    while strikes < max_strikes:
        #Displays the current state of the word
        print(f"\nWord to guess: {display_word(word, guessed_letter)}")
        print(f"Strikes Left: {max_strikes - strikes}")
        #Displays currently guessed letters
        if guessed_letter:
            print("Guessed Letters: ", end= " ")
            for letter in guessed_letter:
                print(letter, end=", ")
            print()
        else: 
            print("You have no correctly guessed letters!")
        #Gets user input for their guess
        guess = input('Guess a letter or type "quit" to quit the game: ').lower()
        #This handles the case where the player may want to quit playing the game
        if guess == "quit":
            print("You have quit the game")
            break
        #Performs a check to make sure the user input is a single and valid letter
        if len(guess) == 1 and guess.isalpha():
            #Checks for duplicate incorrect guesses
            if guess in guessed_letter:
                print("You have guessed this letter previously! Try again")
            else:
                #Adds the letter to the guess list 
                guessed_letter.append(guess)
                #Increments strike if the guess is wrong
                if guess not in word:
                    strikes +=1
                    print(f"Incorrect Guess! You have {max_strikes - strikes} strikes left.")
                else:
                    print("Your guess was correct!")
        else:
            print("You provided an invalid input, enter a single letter.")
        #Checks to see if the word has been correctly guessed
        display = display_word(word, guessed_letter)
        if display == word:
            print(f"\nYou have guessed the word: {word}!")
            break
    else:
        #Prints if the user has used all the strikes avaliable without guessing the word and prints the word 
        print(f"You have lost, the word was {word}")
#Starts the game 
hangman()

