import random
from art import logo

easy_level_turn = 10
hard_level_turn = 5
turns = 0


def check_answer(user_guess, actual_guess, turns):
    if 0 < user_guess < 100:
        if user_guess > actual_guess:
            print( "Too High." )
            return turns - 1
        elif user_guess < actual_guess:
            print( "Too Low." )
            return turns - 1
        else:
            print( f"You got it! The answer is {actual_guess}" )
    else:
        print( "Choose a number between 0 and 100. " )


def set_difficulty():
    level = input( "Choose a Difficulty. Type 'easy' or 'hard'. \n" ).lower()
    if level == 'easy':
        return easy_level_turn
    elif level == 'hard':
        return hard_level_turn
    else:
        print( "Please enter correct value." )


def game():
    print( "I'm thinking of a number between 1 and 100." )
    answer = random.randint( 1, 100 )

    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print( f"You have {turns} attempts remaining to guess the number. " )
        guess = int( input( "Make a guess: " ) )
        turns = check_answer( guess, answer, turns )
        if turns == 0:
            print( "You run out of guesses." )
            return
        elif guess != answer:
            print( "Guess Again." )


if __name__ == "__main__":
    print( logo )
    print( "WELCOME TO THE NUMBER GUESSING GAME!" )
    game()
