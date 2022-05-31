# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

# Required modules and files
from os import system, name
from art import logo

def welcome():
    # Print the logo
    print(logo)

    # Print the welcome message
    print("Welcome to Python Blind Auction!")

def main():
    # Function to clear the screen
    def clear():
        if name == 'nt':
            _ = system('cls')

        else:
            _ = system('clear')

    # Function to find the highest bid
    def find_highest(bids):
        highest = 0
        winner = ""

        for bidder in bids:
            bid_amount = bids[bidder]

            if bid_amount > highest:
                highest = bid_amount
                winner = bidder
        
        print(f"\nThe winner is: {winner}, with the highest bid as: {highest}")

    # Create an empty dictinoary and set the end to False
    bids = {}
    end = False

    # While loop to loop through until the end
    while not end:
        # Ask for the inputs
        username = input("Enter you name: ")
        bid = int(input("Eneter your bid: "))
        others = input("\nIs there any other bidder? Type ('yes' or 'no'): ")

        bids[username] = bid

        if others == "no":
            end = True
            find_highest(bids)

        else:
            clear()

welcome()
main()