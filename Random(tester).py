deck_name = "C:/Users/samue/OneDrive/Desktop/Ankify/Variable/Deckname.txt"
with open(deck_name, 'r') as file:
    Deck = file.read()
print(Deck)