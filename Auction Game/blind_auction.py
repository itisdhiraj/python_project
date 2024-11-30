from art import logo


def find_highest_bidder(bid_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print( f"the Winner of highest bidder is {winner} with bid value ${highest_bid}." )


def auction_method():
    bids = {}
    continue_bidding = True
    while continue_bidding:
        bidder_name = input( "What is your name?: " )
        bid = int( input( "What is your bid? :  $" ) )
        bids[bidder_name] = bid
        # bids = {bidder_name: bid}

        prompt_again = input(
            "Is there any other user who wants to bid? : type 'yes' for yes or 'no' for no. : " ).lower()
        if prompt_again == 'no':
            continue_bidding = False
            find_highest_bidder( bids )
        elif prompt_again == 'yes':
            print( "\n" * 20 )


if __name__ == "__main__":
    print( "WELCOME TO BLIND AUCTION!" )
    print( logo )
    auction_method()
