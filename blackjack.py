import random
import clear_screen
from art import logo

# Deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Shuffle and pick random cards.


def getRandomCard():
    return random.choice(cards)


def getRandom2Cards():
    return random.sample(cards, k=2)

# Result checking function


def announce(playerCount, dealerCount):
    '''Compares the scores and announce the win or lose'''
    if playerCount > 21:
        print("Sorry, you lost.")
    elif (playerCount < 21 and dealerCount < 21) and (dealerCount > playerCount):
        print("Sorry, you lost.")
    elif playerCount <= 21 and playerCount > dealerCount:
        print("You won!")
    elif playerCount == dealerCount:
        print("Draw")
    else:
        print("You lost!")


def play():

    print(logo)

    dealerRandomCards = getRandom2Cards()
    playerRandomCards = getRandom2Cards()
    is_over = False

    def sumScores(cardsInHand):
        # if sum(cards) == 21 and len(cards) == 2:
        #     return 0

        if 11 in cardsInHand and sum(cards) > 21:
            cardsInHand.remove(11)
            cardsInHand.append(1)

        return sum(cardsInHand)

    check = input(
        f"Your cards are {playerRandomCards}, total: {sumScores(playerRandomCards)}\n"
        f"Dealer's card are {dealerRandomCards}, total: {sumScores(dealerRandomCards)}\n"
        f"Do you want another card?\n y/n\n")

    # More cards y/n?

    if check == "y":
        playerRandomCards.append(getRandomCard())
        print(
            f"Your cards are {playerRandomCards} and total:{sumScores(playerRandomCards)}")
        announce(sumScores(playerRandomCards), sumScores(dealerRandomCards))

    if check == "n":
        announce(sumScores(playerRandomCards), sumScores(dealerRandomCards))


while input("BLACKJACK!  - Start a new game y/n?\n") == "y":
    clear_screen.clear()
    play()
