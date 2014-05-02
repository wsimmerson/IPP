# implementation of card game - Memory

import simplegui
import random

# Globals
CARD_WIDTH = 50
CARD_HEIGHT = 80

turn_count = 0
cards = []
click_rotate = 0
shown_cards = []

# Populate Cards
for c in range(8):
    cards.append({"face" : str(c), "matched": False, "showing" : False, "pos":[]})
    cards.append({"face" : str(c), "matched": False, "showing" : False, "pos":[]})

def new_game():
    """
        Set and Re-Set global game variables
    """
    global cards, turn_count
    
    random.shuffle(cards)
    x_cord = 60
    y_cord = 90
    
    for index, c in enumerate(cards):
        
        if index == 8:
            y_cord = 240
            x_cord = 55
            
        c["matched"] = False
        c["showing"] = False
        c["pos"] = [x_cord, y_cord]
        x_cord += 105

    turn_count = 0
    shown_cards = []
    

def mouseclick(pos):
    """
        checks if pos is a valid card
        performs checks and updates accordingly
    """
    global cards, turn_count, shown_cards
       
    for index, card in enumerate(cards):
        if pos[1] > card['pos'][1] - CARD_HEIGHT / 2 and pos[1] < card['pos'][1] + CARD_HEIGHT / 2 and pos[0] < card['pos'][0] + CARD_WIDTH / 2 and pos[0] > card['pos'][0] - CARD_WIDTH / 2:
            if not cards[index]['matched'] and not cards[index]['showing']:                
                
                shown_cards.append(index)                
                
                if len(shown_cards) == 3:
                    for rmv in range(2):
                        cards[shown_cards[0]]['showing'] = False
                        shown_cards.pop(0)
                    
                if len(shown_cards) == 2:
                    turn_count += 1
                    if cards[shown_cards[0]]['face'] == cards[shown_cards[1]]['face']:
                        cards[shown_cards[0]]['matched'] = True
                        cards[shown_cards[1]]['matched'] = True
                
                # Set shown cards
                for shown in shown_cards:
                    cards[shown]['showing'] = True
   
def draw(canvas):
    """
        Draws game board and displays cards
    """
    global label, cards
    label.set_text('Number of Turns: %s'% str(turn_count))
    
    for card in cards:

        if card['matched']:
            color = "Green"
        elif card['showing']:
            color = "Red"
        else:
            color = "Blue"
            
        canvas.draw_polygon([[card['pos'][0] - CARD_WIDTH / 2, card['pos'][1] - CARD_HEIGHT / 2],
                             [card['pos'][0] + CARD_WIDTH / 2, card['pos'][1] - CARD_HEIGHT / 2],
                             [card['pos'][0] + CARD_WIDTH / 2, card['pos'][1] + CARD_HEIGHT / 2],
                             [card['pos'][0] - CARD_WIDTH / 2, card['pos'][1] + CARD_HEIGHT / 2],
                             ],
                            1, color, color)
        
        if card['matched'] or card['showing']:
            canvas.draw_text(card['face'],
                             [card['pos'][0] - 10,
                              card['pos'][1] + 10],
                             36, "White")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 850, 320)
frame.add_button("Restart", new_game)
label = frame.add_label('')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
