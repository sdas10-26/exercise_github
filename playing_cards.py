from random import shuffle

class Card:
    """
    Represents a single card that has a value, name, and suit.

    Attributes:
        suit(str): Suit of the card(club, diamond, hearts, spades).
        value(int): Value of the card ranging from 2-14.
        name(str): Name of the card(jack, king, queen, ace, 2-10).
    """
    def __init__(self,value,suit):
        self.suit = suit
        self.value = value
        name = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        self.name = str(value) if 2 <= value <= 10 else name[value]

    def __str__(self):
        return f"{self.name} of {self.suit}"
    
class Deck:
    """
    Represents a standard deck of 52 cards.

    Attributes:
        cards(list): List of card objects.
    """
    def __init__(self):
        self.cards = [Card(val, suit) for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]
                      for val in range(2, 15)]
        shuffle(self.cards)

    def draw(self):
        """
        Draws and removes the card that is at the top of the deck.

        Returns:
            card: This is the top card of the deck.
        
        Raises:
            RunTimeError: Deck is empty.
        """
        if self.cards:
            return self.card.pop()
        else:
            raise RuntimeError("The deck is empty.")
        

if __name__ == "__main__":
    deck = Deck()
    print("Drawing 5 cards:")
    for _ in range(5):
        print(deck.draw())
        