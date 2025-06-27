from random import randint
import pgzrun

HEIGHT=600
WIDTH=800

start_speed = 10
ITEMS=["bag","battery","bottle","chips"]

final_level=6
current_level=1

#lose the game
game_over=False

#win the game
game_complete=False

items=[]
animations=[]

def draw():
    global items, current_level, game_complete, game_over
    screen.clear()
    screen.blit("bground", (0,0))

    if game_over:
        display_message("GAME OVER", "Try again.")
    elif game_complete:
        display_message("YOU WON", "Well done.")
    else:
        for item in items:
            item.draw()

def display_message(heading,subheading):
    screen.draw.text(heading, fontsize=60, center=(400,300), color="black")
    screen.draw.text(subheading, fontsize=30, center=(330,300), color="blue")

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

#Make items
#1. select random items from ITEMS list
#2. create actors and add it to items list
#3. do the items with correct positions
#4. move the objects down with animation



pgzrun.go()
