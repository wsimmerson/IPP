# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        self.show = True
        
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        if self.show:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                              (pos[0] + CARD_BACK_CENTER[0],
                               pos[1] + CARD_BACK_CENTER[1]),
                              CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        rtn = ''
        for card in self.hand:
            rtn += str(card) + ' '

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        """
            count aces as 1, if the hand has an ace, then add 10 to hand value if 
            it doesn't bust compute the value of the hand, see Blackjack video 
        """
        value = 0
        aces = 0
        for card in self.hand:
            if card.rank == 'A':
                aces += 1
                if aces >= 2 and (value + 11) <= 21:
                    value += 11
                else:
                    value += VALUES[card.get_rank()]
            else:
                value += VALUES[card.get_rank()]
            
        return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        i = 0
        for card in self.hand:
            card.draw(canvas, (pos[0] + (30 * i), pos[1]))
            i += 1
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        card = self.cards[0]
        self.cards.pop(0)
        return card
    
    def __str__(self):
        rtn = ''
        for card in self.cards:
            rtn += str(card) + " "
        
        return rtn



#define event handlers for buttons
def deal():
    global deck, player, dealer, outcome, in_play, score
    if in_play:
        score -= 1
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    for i in range(2):
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
    dealer.hand[0].show = False
    in_play = True
    outcome = "Hit or Stand?"

def hit():
    global outcome, in_play, score
    if not in_play:
        return
    player.add_card(deck.deal_card())
    outcome = "Hit or Stand?"
    if player.get_value() > 21:
        outcome = "Busted. New deal?"
        in_play = False
        score -= 1
    
def stand():
    global outcome, in_play, score, dealer
    if not in_play:
        return
    dealer.hand[0].show = True
    while dealer.get_value() < 17:
        dealer.add_card(deck.deal_card())
    if dealer.get_value() > 21:
        score += 1
        outcome = "Dealer Busted! New deal?"
    elif player.get_value() > dealer.get_value():
        score += 1
        outcome = "You win! New deal?"
    else:
        score -= 1
        outcome = "You lose. New deal?"
    in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", (25, 20), 18, "White")
    canvas.draw_text("Score: " + str(score), (25, 40), 18, "White")
    canvas.draw_text(outcome, (25, 85), 18, "White")
    # draw score
    canvas.draw_text("Hand Value: " + str(player.get_value()), (25, 452), 18, "#eeeecc")
    # draw hands
    dealer.draw(canvas, (40, 120))
    player.draw(canvas, (40, 280))


# initialization frame
frame = simplegui.create_frame("Blackjack", 250, 500)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

