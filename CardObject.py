from dataclasses import dataclass
from enum import IntEnum


class CardType(IntEnum):
    Pokemon = 1
    Trainer = 2
    Energy = 3


def getCardType(cardStr):
    return {
        "Pokémon": CardType.Pokemon,
        "PokÃ©mon": CardType.Pokemon,
        "Trainer": CardType.Trainer,
        "Energy": CardType.Energy
    }.get(cardStr)


class VisualType(IntEnum):
    Normal = 1
    PartialHolo = 2  # PH


def getVisualType(cardStr):
    return {
        "Normal": VisualType.Normal,
        "PH": VisualType.PartialHolo,
    }.get(cardStr)


class CardState(IntEnum):
    InDeck = 1  # Default
    InHand = 2
    InPrizes = 3
    InDiscard = 4
    InLostZone = 5
    InPlay = 6


@dataclass
class Card:
    card_type: CardType
    name: str
    set_name: str
    set_number: int
    visual_type: VisualType
    card_state: CardState = CardState.InDeck

    def __repr__(self):
        return f"{self.card_type.name}: {self.name}"
