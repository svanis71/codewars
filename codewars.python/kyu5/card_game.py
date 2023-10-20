"""
https://www.codewars.com/kata/61fef3a2d8fa98021d38c4e5/python
"""


def make_move(deck_size: int) -> tuple[int, int]:
    cards_taken = 0
    if deck_size % 2 == 1 or ((deck_size // 2) % 2 == 0 and deck_size > 4):
        cards_taken += 1
        deck_size -= 1
    else:
        cards_taken += (deck_size // 2)
        deck_size //= 2
    return cards_taken, deck_size


def card_game(n: int) -> int:
    deck: int = n
    alice: int = 0
    bob: int = 0
    while deck > 0:
        alice_cards, deck = make_move(deck)
        alice += alice_cards
        bob_cards, deck = make_move(deck)
        bob += bob_cards
    return alice
