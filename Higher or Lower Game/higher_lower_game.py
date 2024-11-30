from art import logo, vs
import random
from game_data import data
score = 0

def format_data(account):
    account_name = account["name"]
    account_follower = account["follower_count"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_follower}, {account_descr}, {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

game_should_continue = True

def choice():
    score = 0
    account_b = random.choice( data )
    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data( account_b )}.")

        guess = input("Who has more follower? Type 'A' or 'B': ").lower()
        #clear the screen
        print("\n" * 20)
        print(logo)

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count,b_follower_count)

        if is_correct:
            score +=1
            print("you are right!")
        else:
            print("You are wrong!")



if __name__ == "__main__":
    print(logo)
    print("WELCOME TO HIGHER OR LOWER FOLLOWER GAME!")
    choice()