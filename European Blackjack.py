from time import sleep
from random import shuffle
from os import system


# Value of the card
def card_value(card):
    if card == "A":
        return 11
    elif card in ("J", "Q", "K"):
        return 10
    else:
        return int(card)

# Value of the hand
def hand_value(hand):
    new_hand = hand[:]
    total = 0

    for card in new_hand:
        total += card_value(card)

    while total > 21 and "A" in new_hand:
        pos = new_hand.index("A")
        new_hand[pos] = "1"
        total = 0

        for card in new_hand:
            total += card_value(card)

    return total

# Deal card
def deal_card(hand):
    card = deck.pop()
    hand.append(card)

# Deal to dealer
deal_to_dealer = '''while hand_value(dealerHand) < 17:
    print("\\nDealer takes a card")
    sleep(1.3)
    deal_card(dealerHand)
    print("Dealer's hand:", dealerHand)
    sleep(1.5)'''

while True:

    # Create deck and hands
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4
    playerHand = []
    dealerHand = []

    # Shuffle deck
    for i in range(3):
        print("\rShuffling deck" + "." * (i % 3 + 1), end="")
        sleep(0.45)

    shuffle(deck)

    # Deal cards
    print("\nDealing cards")
    sleep(1.3)

    # First round dealt
    deal_card(playerHand)
    # Dealer's hand dealt
    deal_card(dealerHand)
    # Second round dealt
    deal_card(playerHand)

    # Show hands
    print("\nDealer's hand:", dealerHand)
    sleep(1.3)
    print("Your hand:", playerHand)
    sleep(1.3)

    # Outcomes
    while True:

        # If player gets blackjack
        if hand_value(playerHand) == 21:
            if hand_value(dealerHand) < 10:
                print("\nBlackjack! You win!")
            else:
                print("\nBlackjack!")
                sleep(1.3)
                print("\nTime to see what the dealer gets.")
                sleep(1.3)
                deal_card(dealerHand)
                print("\nDealer's hand:", dealerHand)
                sleep(1.3)

                if hand_value(dealerHand) == 21:
                    print("\nDealer got blackjack! It's a draw!")
                else:
                    print("\nDealer scored {}. You win!".format(hand_value(dealerHand)))
            break

        else:
            while True:
                if hand_value(playerHand) == 21:
                    print("\nYou scored 21!")
                    sleep(1.3)
                    print("\nTime to see what the dealer gets.")
                    sleep(1.3)

                    exec(deal_to_dealer)  # Dealer deals himself

                    if hand_value(dealerHand) == 21:
                        if len(dealerHand) == 2:
                            print("\nDealer got blackjack! You lose!")
                        else:
                            print("\nDealer scored 21. It's a draw!")
                    elif hand_value(dealerHand) > 21:
                        print("\nDealer busts! You win")
                    elif hand_value(playerHand) > hand_value(dealerHand):
                        print("\nDealer scored {}. You win!".format(hand_value(dealerHand)))
                    break

                elif hand_value(playerHand) > 21:
                    print("\nYou bust!\nDealer wins!")
                    break

                decision = input("\nWould you like to hit (h) or stand (s)? ")

                if decision.lower() in ("stand", "s"):
                    print("\nYou scored {}.".format(hand_value(playerHand)))
                    sleep(1.3)
                    print("\nTime to see what the dealer gets.")
                    sleep(1.3)

                    exec(deal_to_dealer)  # Dealer deals himself

                    if hand_value(dealerHand) == 21 and len(dealerHand) == 2:
                        print("\nDealer got blackjack! You lose!")
                    elif hand_value(playerHand) < hand_value(dealerHand) <= 21:
                        print("\nDealer scored {}. Dealer wins!".format(hand_value(dealerHand)))
                    elif hand_value(dealerHand) == hand_value(playerHand):
                        print("\nDealer scored {}. It's a draw!".format(hand_value(dealerHand)))
                    elif hand_value(dealerHand) > 21:
                        print("\nDealer busts! You win!")
                    else:
                        print("\nDealer scored {}. You win!".format(hand_value(dealerHand)))
                    break
                elif decision.lower() in ("hit", "h"):
                    print("\nDealing card")
                    sleep(1)
                    deal_card(playerHand)
                    print("Your hand:", playerHand)
                    continue
                else:
                    print("Invalid response")

            break

    sleep(1.3)

    # Play again?
    while True:
        answer = input("\nPlay again? (y/n): ")
        if answer.lower() in ("y", "n"):
            break
        print("Invalid input.")

    if answer.lower() == "y":
        print("\nStarting new game...")
        sleep(1.3)
        system('cls')
        continue

    else:
        break
