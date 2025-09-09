# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)
print("Welcome to the secret auction program.")
#print("\n" * 100)
want_continue = "yes"
bid = {}
count = 0
while want_continue == "yes":
    name = input("What is your name?: ")
    bid[name] = int(input("What is your bid?: $"))
    want_continue = input("Do you want to continue? Type 'yes' or 'no'.\n").lower()
    print("\n" * 100)
    #print(bid)

highest_bidder = ""
highest_bid = 0
for bid_item in bid:
    if bid[bid_item] >= highest_bid:
        highest_bid = bid[bid_item]
        highest_bidder = bid_item
print("\n" * 100)
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

#max function
    #max(dict, key = dict.get)