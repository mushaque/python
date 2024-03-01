# import re
# txt="^The a Spain$"
# x=re.search("^T.*.*",txt)
# print(x)

# if x:
#     print("Yes!We have a match")
# else:
#     print("No match")


# # The findall() Function
# # Print a list of all matches:

import random
import string

def generate_deck():
 deck = []
letters = string.ascii_letters
numbers = string.digits
while len(deck)<52:
    card = ""
    for i in range(6):
        alpha_char = random.choice(letters+numbers)
        # print(alpha_char)
        card = card + alpha_char
        # print(card)

    if card in deck:
        continue
    else:
        deck.append(card)

# print(deck)


def replace_card_name(deck, old_card_name, new_card_name, num_replacements):
    for _ in range(num_replacements):
        # Select a random index in the deck
        random_index = random.randint(0, len(deck) - 1)

        # Replace the old card name with the new card name at the selected index
        deck[random_index] = new_card_name

    return deck

deck = generate_deck()
print("Original Deck:")
print(deck)

old_card_name = input("Enter the name of the card to replace: ")
new_card_name = input("Enter the new name of the card: ")

deck_with_replacements = replace_card_name(deck, old_card_name, new_card_name, 6)
print("\nDeck with Card Name '{}' replaced in 6 places with '{}'".format(old_card_name, new_card_name))
print(deck_with_replacements)
