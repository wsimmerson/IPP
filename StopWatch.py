###############################################
#
#	Stop Watch Game
#	Interactive Programming with Python
#	Coursera.org
#	http://www.codeskulptor.org required to run
#
#	Accuracy of the SimpleGUI timer is questionable
#	decided to use python time module to calculate
#	the number of milliseconds passed between timer
#	calls (despite timer being set to run every 1ms)
#
###############################################
import simplegui
from time import time

# define global variables
interval = 1
game_time = 0
start_time = 0
score = 0
stops = 0

def format(t):
    """
        format the time for display
        Minutes:Seconds.Tenths_of_Seconds
    """
    t = int(t)
    minutes = (t // 1000) // 60
    seconds = (t // 1000) % 60
    tenths = (t // 100) % 10
    
    # Inject a leading 0 where necessary
    if seconds < 10:
        seconds = "0" + str(seconds)
    
    return "%s:%s.%s" % (minutes, seconds, tenths)
    
def start():
    """
        starts the timer if it isn't already running
    """
    global start_time
    
    if not timer.is_running():
        timer.start()
        start_time = time() * 1000 - game_time
    
def stop():
    """
        Checks if the timer is running, stops timer and increases
        stops count and calculates if point is scored.
    """
    global stops, score
    
    if timer.is_running():
        stops += 1
        timer.stop()
    
        if (game_time // 100) % 10 == 0:
            score += 1
    
def reset():
    """
        Reset Globals to start a new game
    """
    global game_time, score, stops, start_time
    timer.stop()
    game_time = 0
    score = 0
    stops = 0
    start_time = 0
    
def time_handler():
    """
        Increases global game_time
    """
    global game_time
    game_time = (time() * 1000 - start_time)
    

def draw(canvas):
    """
        Draws the current score and time calculation
    """
    canvas.draw_text(str(score) + "/" + str(stops), [220, 40], 36, "Green")
    canvas.draw_text(format(game_time), [100,150], 36, "White")
    
# create frame
frame = simplegui.create_frame("Stop Watch", 300, 300)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, time_handler)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# start frame
frame.start()

