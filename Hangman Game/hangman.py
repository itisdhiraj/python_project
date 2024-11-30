import random
import hangman_words
from art import logo


def game_hangman():
    # words_list = ["secret", "apple", "water", "music"]
    random_word = random.choice( hangman_words.words_list )

    # print( random_word )
    blank = ""
    word_length = len( random_word )
    lives = 5
    for position in range( word_length ):
        blank += "_"
    blank_list = list( blank )

    game_over = False

    while not game_over:
        print( f"You have {lives} remaining chances." )

        # User to guess the letter
        guess = input( "Guess a letter : " ).lower()

        if guess in blank_list:
            print( f"You have already guessed {guess}. You lose a life." )
            lives -= 1
            if lives == 0:
                game_over = True
                print( "You lose!" )
                print( f"The correct word is {random_word}." )

        display = ""
        for letter in random_word:
            if letter == guess:
                display += letter
                blank_list.append( letter )
            elif letter in blank_list:
                display += letter
            else:
                display += "_"
        print( "Word to Display: " + display )

        if guess not in random_word:
            lives -= 1
            print( f"You guessed {guess}, that's not in the word. You lose a life." )
            if lives == 0:
                game_over = True
                print( "You lose!" )
                print( f"The correct word is {random_word}." )

        if "_" not in display:
            game_over = True
            print( "You won!" )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print( logo )
    print( "Welcome to the game of HANGMAN." )
    game_hangman()
