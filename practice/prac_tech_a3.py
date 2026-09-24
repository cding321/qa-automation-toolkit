from collections import deque


class Card:
    def __init__(self, rank):
        self.rank = rank

    def __repr__(self):
        return str(self.rank)


class Deck:
    def __init__(self):
        self.cards = deque()

    def draw(self):
        return self.cards.popleft()

    def add(self, card):
        self.cards.append(card)


class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.deck = Deck()

    def draw(self):
        return self.deck.draw()

    def has_cards(self):
        return len(self.deck.cards) > 0


class Game:
    def __init__(self, n, cards):
        self.players = [Player(i + 1) for i in range(n)]
        self.rounds = 0
        self.deal(cards)

    def deal(self, cards):
        for i, rank in enumerate(cards):
            player = self.players[i % len(self.players)]
            player.deck.add(Card(rank))