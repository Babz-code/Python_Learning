import art
print(art.logo)
name_price_dic = {}
auction = True
while auction:
    print("Welcome to the Blind Auction")
# TODO-1: Ask the user for input
    name = input("What is your name?").lower()
    bid_price = int(input("What is your bid price? $"))

# TODO-2: Save data into dictionary {name: price}
    name_price_dic[name] = bid_price

# TODO-3: Whether if new bids need to be added
    any_more_bids = input("Are there any other bids? Yes or No\n").lower()
    if any_more_bids == "yes":
        auction = True
        print("\n" * 100)
    else:
        auction = False
# TODO-4: Compare bids in dictionary
def highest_bidder(new_bid_list):
    highest_bid = 0
    winner = ""
    for x in new_bid_list:
        bid_amount = name_price_dic[x]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = x

    print(f"The winner is {winner} with a bid price of ${highest_bid}")

highest_bidder(name_price_dic)