# # x=3
# # y=4
# # print(x+y)

# # # Lists

# # grocery_list = ['choclates','fruits','vegetables','choclates','choclates']
# # # quantity_list = [1,3,4,5]
# # # price_list = [0.5,6.3,7.2]

# # # print entire list
# # print(grocery_list)

# # # # print 1st two items
# # # print(grocery_list[:2])

# # # # print 3rd item
# # # print(grocery_list[2])

# # # grocery_list[2] = 'Carrots'

# # # # print entire list
# # # print(grocery_list)

# # # # print length of list
# # # print(len(grocery_list))

# # # #remove last item and assign to new variable
# # # last_item = grocery_list.pop()

# # # print(gro
# # # print(grocery_list,last_item)
# # # # insert an item at any given place
# # # grocery_list.insert(2,'pens')
# # # print(grocery_list)

# # #add new item at end
# # grocery_list.append('water bottle')
# # # remove a specific item
# # grocery_list.remove('choclates')
# # print(grocery_list)
# # print(grocery_list.count('choclates'))


import random
import string

def generate_deck():
    deck = []
    letters = string.ascii_letters
    numbers = string.digits

    while len(deck) < 52:
        card = ""
        for i in range(6):
            alpha_char = random.choice(letters + numbers)
            card += alpha_char
        deck.append(card)

    return deck

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


def calculate_probability(num_replacements, total_cards):
    probability = 1
    for i in range(num_replacements):
        probability *= (total_cards - i) / total_cards
    return probability

num_replacements = 6
total_cards = 52

probability = calculate_probability(num_replacements, total_cards)
print("Probability of having 52 unique cards after replacing one card in 6 different places:", probability)

