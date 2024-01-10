"""
A simple Pokemon TCG card deck simulation that parses deck exports from Pokemon TCG Live
"""

import os

from CardDeck import CardDeck
from CardObject import CardState

if __name__ == "__main__":
    input_file = "decklist.txt"
    file = open(input_file, "r")
    file_contents = file.read()
    # Trim out blank lines
    file_contents = os.linesep.join([s for s in file_contents.splitlines() if s])
    deck = CardDeck(file_contents.splitlines())
    def simulateBeginning():
        drawCards = deck.playCards(7, toState = CardState.InHand)
        print("You drew the following cards:")
        for card in drawCards:
            print(card)
        print()
        drawCards = deck.playCards(6, toState = CardState.InPrizes)
        print(f"If no mulligans happened, these would be your prize cards:")
        for card in drawCards:
            print(card)

    def simulateDrawingStartingCard():
        gotPokemon = False
        attempts = 0
        targetCard = "Morpeko"
        while not gotPokemon:
            drawCards = deck.simulateStartingHand()
            for card in drawCards:
                if card.name == targetCard:
                    gotPokemon = True
                    break
            attempts += 1

        print(f"It took {attempts} attempt(s) to get {targetCard}.")


    simulateBeginning()
