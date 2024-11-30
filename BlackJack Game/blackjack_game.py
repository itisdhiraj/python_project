import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    selection = random.choice( cards )
    return selection


def calculate_score(cards):
    if sum( cards ) == 21 and len( cards ) == 2:
        return 0
    if 11 in cards and sum( cards ) > 21:
        cards.remove( 11 )
        cards.append( 1 )

    return sum( cards )


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "lose, Opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "lose, You went Over"
    elif c_score > 21:
        return "You win, Opponent went over"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    for card in range( 2 ):
        user_cards.append( deal_card() )
        computer_cards.append( (deal_card()) )

    while not is_game_over:
        user_score = calculate_score( cards=user_cards )
        computer_score = calculate_score( cards=computer_cards )
        print( f"Your cards : {user_cards} and current user score is : {user_score}" )
        print( f"Computer's first cards : {computer_cards[0]}" )

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input( "Type 'y' to get another card, type 'n' to pass: " ).lower()
            if user_should_deal == "y":
                user_cards.append( deal_card() )
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append( deal_card() )
        computer_score = calculate_score( computer_cards )

    print( f"Your final cards : {user_cards} and user final score is : {user_score}" )
    print( f"Computer's Final cards : {computer_cards} and Computer's final score is : {computer_score}" )

    print( compare( user_score, computer_score ) )


if __name__ == "__main__":
    print( logo )
    print( "WELCOME TO BLACKJACK CARD GAME! " )

    while input( "Do You want to play a game of blackjack? Type 'y' or 'n': " ).lower() == 'y':
        print( "\n" * 50 )
        print( logo )
        play_game()
