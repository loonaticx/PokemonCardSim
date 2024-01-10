from CardObject import getCardType, Card, CardState
import random


class CardDeck:
    """
    The deck does not control the state of a card.
    """

    def __init__(self, decklist):
        self.deck = self.buildDeck(decklist)
        assert len(self.deck) == 60

    def getSectionInfo(self, header):
        header = header.replace(":", "").split(" ")
        header[0] = getCardType(header[0])
        header[-1] = int(header[-1])
        return header

    def buildDeck(self, decklist):
        cardDecklist = []
        currentLine = 0
        deck_pokemon_header = decklist[currentLine]  # Pokémon: 10
        # 10 lines of cards, but not 10 qty
        cardSections = [
            self.getSectionInfo(deck_pokemon_header),
        ]
        # Trainers
        cardSections.append(self.getSectionInfo(decklist[int(cardSections[0][1]) + 1]))
        # Energy
        cardSections.append(self.getSectionInfo(decklist[cardSections[0][1] + cardSections[1][1] + len(cardSections)]))
        for cardSection in cardSections:
            currentLine += 1
            cardType, cardLines = cardSection
            newLine = currentLine
            for line in range(newLine, int(cardLines) + newLine):
                cardLine = decklist[line].split(" ")
                if cardLine[-1] != "PH":
                    cardLine.append("Normal")
                qty = int(cardLine[0])
                visualType = cardLine[-1]
                setNumber = cardLine[-2]
                setName = cardLine[-3]
                cardName = " ".join(cardLine[1:-3])
                for count in range(qty):
                    cardDecklist.append(Card(
                        card_type = cardType,
                        name = cardName,
                        set_name = setName,
                        set_number = setNumber,
                        visual_type = visualType
                    ))
                currentLine += 1
        return cardDecklist

    def playCards(self, amt, toState, shuffleFirst=True):
        # Note: This is only effective for an initial draw, since it does not consider the current
        # states of any of the cards.
        playedCards = []
        if shuffleFirst:
            random.shuffle(self.deck)
        validCards = 0
        i = 0
        # Todo: This should be moved somewhere else since it would get really redundant long-game
        # But we can focus on a separate class for a state manager.
        while validCards != amt:
            card = self.deck[i]
            if card.card_state == CardState.InDeck:
                playedCards.append(card)
                validCards += 1
                card.card_state = toState
            i += 1
        return playedCards

    def simulateStartingHand(self, amt: int = 7, shuffleFirst=True):
        playedCards = []
        if shuffleFirst:
            random.shuffle(self.deck)
        for i in range(amt):
            card = self.deck[i]
            playedCards.append(card)
        return playedCards
