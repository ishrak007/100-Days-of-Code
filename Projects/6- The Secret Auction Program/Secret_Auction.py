from replit import clear
from auction_art import *
print(logo)
print("Welcome to The Secret Auction Program.")

# Interface
bid_done = False
bid_entries = {}
while bid_done == False:
    name = input("Type your name: ")
    print(f"Your name: {name}")
    bid = int(float(input("Type your bid: $")))
    print(f"Your bid: {bid}")
    bid_entries[name] = bid
    more_bids = input("Are there any other bidders? Type 'y' if yes or 'n' if no: ")
    if more_bids == 'y':
        clear()
        continue
    elif more_bids == 'n':
        bid_done = True
    else:
        print("Invalid Key.")
        continue

bidder_names = list(bid_entries.keys())
bid_values = list(bid_entries.values())
# print(bidder_names)
# print(bid_values)

# Winner Finding
bid_count = 0
highest_bid = bid_values[0]
highest_bidder = ""
for i in bid_values:
    bid_count = i
    if highest_bid < bid_count:
        highest_bid = bid_count
highest_bidder = bidder_names[bid_values.index(highest_bid)]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")