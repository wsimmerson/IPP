# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 10
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

paddle1_pos = []
paddle2_pos = []
paddle1_vel = []
paddle2_vel =[]
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, -1]
score1 = 0
score2 = 0

def spawn_ball(direction):
    """
        initialize ball_pos and ball_vel for new bal in 
        middle of table if direction is RIGHT, the ball's 
        velocity is upper right, else upper left
    """
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction:
        ball_vel[0] = random.randrange(1, 3)
        ball_vel[1] = 0 - random.randrange(1, 3)
    else:
        ball_vel[0] = 0 - random.randrange(1, 3)
        ball_vel[1] = 0 - random.randrange(1, 3)
    

def new_game():
    """
        Reset Globals for a new game
    """
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]
    
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    
    score1 = 0
    score2 = 0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # Update Ball Position
    # Ball hits top or bottom of screen updates ball_vel
    if ball_pos[1] - BALL_RADIUS <= 0:
        ball_vel[1] = abs(ball_vel[1]) + 1
        
    elif ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = 0 - ball_vel[1] - 1
        
    # Ball hits gutters or paddles
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if ball_pos[1] < paddle1_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] > paddle1_pos[1] - HALF_PAD_HEIGHT:
            ball_vel[0] = abs(ball_vel[0]) + 1
        else:
            score2 += 1
            spawn_ball(True)
    
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if ball_pos[1] < paddle2_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] > paddle2_pos[1] - HALF_PAD_HEIGHT:
            ball_vel[0] = 0 - ball_vel[0] - 1
        else:
            score1 += 1
            spawn_ball(False)
            
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # Draw Ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # Update Left Paddle Position
    if paddle1_pos[1] + HALF_PAD_HEIGHT + paddle1_vel[1] < HEIGHT and paddle1_pos[1] - HALF_PAD_HEIGHT + paddle1_vel[1] > 0:
        paddle1_pos[1] += paddle1_vel[1]
        
    # Update Right Paddle Position
    if paddle2_pos[1] + HALF_PAD_HEIGHT + paddle2_vel[1] < HEIGHT and paddle2_pos[1] - HALF_PAD_HEIGHT + paddle2_vel[1] > 0:
        paddle2_pos[1] += paddle2_vel[1]
    
    # Draw Left Paddle
    c.draw_line([paddle1_pos[0],
                 paddle1_pos[1] - HALF_PAD_HEIGHT],
                [paddle1_pos[0],
                 paddle1_pos[1] + HALF_PAD_HEIGHT],
                PAD_WIDTH, 'White')
    
    # Draw Right Paddle
    c.draw_line([paddle2_pos[0],
                 paddle2_pos[1] - HALF_PAD_HEIGHT],
                [paddle2_pos[0],
                 paddle2_pos[1] + HALF_PAD_HEIGHT],
                PAD_WIDTH, 'White')
    
    # draw scores
    score1_tmp, score2_tmp = str(score1), str(score2)
    
    # keep scores less than 100 at two digits so it's 
    # easier to keep centered.
    if score1 < 10:
        score1_tmp = "0" + str(score1)
    if score2 < 10:
        score2_tmp = "0" + str(score2)
        
    score_text = score1_tmp + "   " + score2_tmp
    score_text_size = frame.get_canvas_textwidth(score_text, 36)
    
    c.draw_text(score_text, [(WIDTH / 2) - (score_text_size / 2), 40], 36, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    # Left Paddle
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel[1] += 3
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel[1] -= 3
    
    # Right Paddle
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += 3
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= 3
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    # Left Paddle
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel[1] = 0
    
    # Right Paddle
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
        
def new_game_button():
    new_game()
    spawn_ball(True)
        

# Create Frame and set handlers
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background("006400")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('New Game', new_game_button)


# Start a game
new_game()
frame.start()
