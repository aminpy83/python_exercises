name = input("tell me your name: ")
bid = int(input("bid: $"))
x = input("is there any bidder left? ")
bidders = {name : bid}

while x.lower() == "yes" :
    new = {}
    name = input("name: ")
    bid = int(input("bid: "))
    bidders.update({name : bid})
    x = input("is there any bidder left? ")

bidders = sorted(bidders.items())
print(f"winner is {bidders[0][0] } with ${bidders[0][1]} ")
